from core.api_client import APIClient

class GitHubAPI:
    def __init__(self, token: str = None):
        headers = {'Accept': 'application/vnd.github.v3+json'}
        if token:
            headers['Authorization'] = f'token {token}'
        self.client = APIClient('https://api.github.com', headers=headers)

    def list_user_repos(self, username: str, per_page: int = 30):
        resp = self.client.get(f'/users/{username}/repos', params={'per_page': per_page})
        return resp.json()

    def repo_info(self, owner: str, repo: str):
        resp = self.client.get(f'/repos/{owner}/{repo}')
        return resp.json()
