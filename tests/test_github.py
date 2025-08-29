from integrations.github_api import GitHubAPI

def test_list_repos():
    gh = GitHubAPI()
    repos = gh.list_user_repos('octocat', per_page=5)
    assert isinstance(repos, list)
