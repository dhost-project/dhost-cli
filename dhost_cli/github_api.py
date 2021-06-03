from .dhost_cli import DhostAPI


class GithubManagement(DhostAPI):

    def me(self):
        uri = 'v1/github/me/'
        response = self.get(uri=uri)
        print(response.json())

    def list(self):
<<<<<<< HEAD
        uri = 'v1/github/'
        response = self.get(uri=uri)
        print(response.json())

    def fetch_all(self):
        """Update the repo from the Github API"""
        uri = 'v1/github/fetch'
        response = self.get(uri=uri)
        print(response.json())

    def retrieve(self, repo_id):
        uri = f'v1/github/{repo_id}/'
        response = self.get(uri=uri)
        print(response.json())

    def fetch_repo(self, repo_id):
        """Update the repo from the Github API"""
        uri = f'v1/github/{repo_id}/fetch/'
=======
        uri = 'v1/github/repos/'
>>>>>>> 8687310... feat: repo name
        response = self.get(uri=uri)
        print(response.json())

    def scopes(self):
        uri = 'v1/github/scopes/'
        response = self.get(uri=uri)
        print(response.json())
