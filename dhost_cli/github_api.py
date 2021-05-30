from .dhost_cli import DhostAPI
from .utils import get_user_str_input


class GithubManagement(DhostAPI):

    def list(self):
        uri = 'v1/github/repositories/'
        response = self.get(uri=uri)
        print(response.json())
