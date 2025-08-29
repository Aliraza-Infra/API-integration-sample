from utils.logger import setup_logging
from integrations.github_api import GitHubAPI
import os

setup_logging()

def main():
    gh = GitHubAPI()
    username = os.getenv('GITHUB_USER', 'octocat')
    repos = gh.list_user_repos(username, per_page=10)
    print(f"Found {len(repos)} repos for {username}")
    for r in repos[:10]:
        print('-', r.get('full_name'))

if __name__ == '__main__':
    main()
