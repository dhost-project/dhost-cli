from .dhost_cli import DhostAPI


class UserManagement(DhostAPI):

    def read(self):
        uri = 'v1/users/me/'
        response = self.get(uri=uri)
        print(response.json())
