from ..utils.timer_base import TimerBase

class GitHubTimer:
    def __init__(self, syncer, interval_minutes):
        self.syncer = syncer
        interval_seconds = max(1, interval_minutes) * 60
        self.timer_base = TimerBase(self._sync_callback, interval_seconds)
    
    def start(self):
        self.timer_base.start()
    
    def stop(self):
        self.timer_base.stop()
    
    def _sync_callback(self):
        self.syncer.sync_if_changed()