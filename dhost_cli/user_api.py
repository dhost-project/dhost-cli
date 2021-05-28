from .dhost_cli import DhostAPI
from .utils import get_user_str_input


class UserManagement(DhostAPI):
    def read(self):
        uri = 'v1/users/me/'
        response = self.get(uri=uri)
        print(response.json())
