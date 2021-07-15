from dhost_cli.api.utils import basic_print

ME_URL = 'users/me/'

def me(self):
    uri = ME_URL
    response = self.get(uri=uri)
    basic_print(response.json())
