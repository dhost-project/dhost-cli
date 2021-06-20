from dhost_cli.api.utils import basic_print

LIST_DAPPS_URL = 'v1/dapps/'
RETRIEVE_DAPP_URL = 'v1/dapps/{dapp_slug}/'


def list(self):
    uri = LIST_DAPPS_URL
    response = self.get(uri=uri)
    basic_print(response.json(), many=True)


def retrieve(self, dapp_slug):
    uri = RETRIEVE_DAPP_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    basic_print(response.json())
