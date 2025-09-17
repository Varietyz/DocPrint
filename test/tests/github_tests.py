import os
import time
from docprint import docPrint, docFlush, docPrintFile, enableGitCommits

class GitHubIntegrationTest:
    def run(self):
        print("Testing GitHub integration...")
        
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except ImportError:
            pass
        
        token = os.getenv('GITHUB_TOKEN')
        repo = os.getenv('GITHUB_REPO', 'test-user/test-repo')
        
        if not token:
            print("  GITHUB_TOKEN not found - skipping GitHub tests")
            print("  Set GITHUB_TOKEN environment variable to test GitHub integration")
            return
        
        if repo == 'test-user/test-repo':
            print("  GITHUB_REPO not set - using default test repository")
            print("  Set GITHUB_REPO environment variable for your test repository")
        
        #self._test_github_sync(token, repo)
    
    def _test_github_sync(self, token, repo):
        try:
            print(f"  Testing GitHub sync with repo: {repo}")
            enableGitCommits(True, token=token, repo=repo, interval_minutes=1)
            print("  GitHub sync enabled")
            
            docPrintFile("github_test.md")
            docPrint('text', 'GitHub Test', f'Testing GitHub integration at {time.strftime("%Y-%m-%d %H:%M:%S")}')
            docPrint('table', 'GitHub Test Data', [
                {'feature': 'Authentication', 'status': 'Working'},
                {'feature': 'Repository Access', 'status': 'Verified'},
                {'feature': 'Content Sync', 'status': 'Testing'}
            ])
            docPrint('alert', 'GitHub Integration', 'This content should sync to GitHub', alert_type='success')
            
            docFlush()
            print("  GitHub test content generated")
            
            time.sleep(2)
            docPrint('text', 'GitHub Update', f'Updated at {time.strftime("%Y-%m-%d %H:%M:%S")}')
            docPrint('bullets', 'Test Results', [
                'GitHub authentication successful',
                'Repository access verified',
                'Content synchronization active'
            ])
            
            docFlush()
            print("  GitHub update content added")
            
            print("  Waiting 65 seconds for GitHub sync...")
            for i in range(65):
                if i % 10 == 0:
                    print(f"    {65-i} seconds remaining...")
                time.sleep(1)
            
            enableGitCommits(False)
            print("  GitHub sync disabled")
            print("  GitHub integration test complete")
            print(f"  Check your repository: https://github.com/{repo}")
            
        except ValueError as e:
            raise AssertionError(f"GitHub configuration error: {e}")
        except Exception as e:
            raise AssertionError(f"GitHub integration error: {e}")