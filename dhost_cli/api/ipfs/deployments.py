LIST_DEPLOYMENTS_URL = 'v1/ipfs/{dapp_slug}/deployments/'
RETRIEVE_DEPLOYMENT_URL = 'v1/ipfs/{dapp_slug}/deployments/{id}/'


def list(self, dapp_slug):
    uri = LIST_DEPLOYMENTS_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    print(response.json())


def retrieve(self, dapp_slug, id):
    response = self.get(uri=RETRIEVE_DEPLOYMENT_URL.format(dapp_slug, id))
    print(response.json())
