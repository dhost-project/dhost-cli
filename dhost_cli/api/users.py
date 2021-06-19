from dhost_cli.api.utils import basic_print

def me(self):
    uri = 'v1/users/me/'
    response = self.get(uri=uri)
    basic_print(response.json())
