from .auth import GitHubAuth
from .timer import GitHubTimer
from .content_reader import ContentReader
from .change_detector import ChangeDetector
from .api_client import APIClient
from .sync_coordinator import SyncCoordinator

class GitHubSyncer:
    def __init__(self, token, repo, file_handler):
        self.auth = GitHubAuth(token, repo)
        self.file_handler = file_handler
        self.timer = None
        self.is_enabled = False
        
        self.content_reader = ContentReader(file_handler)
        self.change_detector = ChangeDetector()
        self.api_client = APIClient(self.auth)
        self.sync_coordinator = SyncCoordinator(
            self.content_reader, 
            self.change_detector, 
            self.api_client, 
            file_handler
        )
    
    def enable(self, interval_minutes=1):
        if not self.auth.validate_repo_access():
            raise ValueError(f"Cannot access repository: {self.auth.repo}")
        
        self.is_enabled = True
        self.timer = GitHubTimer(self, interval_minutes)
        self.timer.start()
    
    def disable(self):
        self.is_enabled = False
        if self.timer:
            self.timer.stop()
    
    def sync_if_changed(self):
        if not self.is_enabled:
            return
        
        self.sync_coordinator.sync_if_changed()