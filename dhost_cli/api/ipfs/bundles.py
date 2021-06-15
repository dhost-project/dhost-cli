LIST_BUNDLES_URL = 'v1/ipfs/{dapp_slug}/bundles/'
RETRIEVE_BUNDLE_URL = 'v1/ipfs/{dapp_slug}/bundles/{id}'


def list(self, dapp_slug):
    uri = LIST_BUNDLES_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    print(response.json())


def retrieve(self, dapp_slug, id):
    uri = RETRIEVE_BUNDLE_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.get(uri=uri)
    print(response.json())
