from dhost_cli.api.utils import basic_print

LIST_LOGS_URL = 'v1/ipfs/{dapp_slug}/logs/'
RETRIEVE_LOG_URL = 'v1/ipfs/{dapp_slug}/logs/{id}/'


def list(self, dapp_slug):
    uri = LIST_LOGS_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    basic_print(response.json(), many=True)


def retrieve(self, dapp_slug, id):
    uri = RETRIEVE_LOG_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.get(uri=uri)
    basic_print(response.json())
