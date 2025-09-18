import urllib.request
import urllib.error

class GitHubAuth:
    def __init__(self, token, repo):
        self.token = token
        self.repo = repo
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        }
    
    def validate_repo_access(self):
        url = f'https://api.github.com/repos/{self.repo}'
        try:
            req = urllib.request.Request(url, headers=self.headers)
            urllib.request.urlopen(req)
            return True
        except urllib.error.HTTPError:
            return False