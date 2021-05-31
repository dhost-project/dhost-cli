from .dhost_cli import DhostAPI
from .utils import get_user_str_input


class GithubManagement(DhostAPI):

    def me(self):
        uri = 'v1/github/me/'
        response = self.get(uri=uri)
        print(response.json())

    def list(self):
        uri = 'v1/github/repositories/'
        response = self.get(uri=uri)
        print(response.json())

    def scopes(self):
        uri = 'v1/github/scopes/'
        response = self.get(uri=uri)
        print(response.json())
