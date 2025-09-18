import base64
import urllib.request
import urllib.error
from ..utils.json_utils import dumps, loads
from ..utils.error_utils import ErrorReporter

class APIClient:
    def __init__(self, auth):
        self.auth = auth
    
    def push_content(self, file_path, content):
        try:
            sha = self._get_file_sha(file_path)
            
            data = {
                'message': f'DocPrint: update {file_path}',
                'content': base64.b64encode(content.encode('utf-8')).decode('utf-8')
            }
            
            if sha:
                data['sha'] = sha
            
            url = f'https://api.github.com/repos/{self.auth.repo}/contents/{file_path}'
            req = urllib.request.Request(
                url, 
                data=dumps(data).encode('utf-8'), 
                headers=self.auth.headers,
                method='PUT'
            )
            
            urllib.request.urlopen(req)
            return True
            
        except Exception as e:
            ErrorReporter.report_network_error("push", f"GitHub repo {self.auth.repo}", e)
            return False
    
    def _get_file_sha(self, file_path):
        try:
            url = f'https://api.github.com/repos/{self.auth.repo}/contents/{file_path}'
            req = urllib.request.Request(url, headers=self.auth.headers)
            response = urllib.request.urlopen(req)
            data = loads(response.read().decode('utf-8'))
            return data.get('sha')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise