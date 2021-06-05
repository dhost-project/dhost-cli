def list(self):
    uri = 'v1/github/'
    response = self.get(uri=uri)
    print(response.json())


def fetch_all(self):
    """Update all repos from the Github API"""
    uri = 'v1/github/fetch_all'
    response = self.get(uri=uri)
    print(response.json())


def retrieve(self, repo_id):
    uri = f'v1/github/{repo_id}/'
    response = self.get(uri=uri)
    print(response.json())


def fetch_repo(self, repo_id):
    """Update the repo from the Github API"""
    uri = f'v1/github/{repo_id}/fetch/'
    response = self.get(uri=uri)
    print(response.json())
