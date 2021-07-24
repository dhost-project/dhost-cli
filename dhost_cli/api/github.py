from dhost_cli.api.utils import basic_print

LIST_REPOSITORIES = "github/repositories/"
FETCH_ALL_REPOSITORIES = "github/repositories/fetch_all/"
RETRIEVE_REPOSITORIES = "github/repositories/{id}/"
FETCH_REPOSITORIES = "github/repositories/{id}/fetch/"
FETCH_BRANCHES_REPOSITORIES = "github/repositories/{id}/fetch_branches/"


def list(self):
    uri = LIST_REPOSITORIES
    response = self.get(uri=uri)
    basic_print(response.json(), many=True)


def fetch_all(self):
    """Update all repos from the Github API."""
    uri = FETCH_ALL_REPOSITORIES
    response = self.get(uri=uri)
    basic_print(response.json(), many=True)


def retrieve(self, repo_id):
    uri = RETRIEVE_REPOSITORIES.format(id=repo_id)
    response = self.get(uri=uri)
    basic_print(response.json())


def fetch_repo(self, repo_id):
    """Update the repo from the Github API."""
    uri = FETCH_REPOSITORIES.format(id=repo_id)
    response = self.get(uri=uri)
    basic_print(response.json())


def fetch_branches(self, repo_id):
    """Update the repo branches from the Github API."""
    uri = FETCH_BRANCHES_REPOSITORIES.format(id=repo_id)
    response = self.get(uri=uri)
    basic_print(response.json())
