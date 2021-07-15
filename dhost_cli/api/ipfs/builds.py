LIST_BUILDS_URL = "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/builds/"
RETRIEVE_BUILD_URL = "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/builds/{id}/"


def list(self, dapp_slug):
    uri = LIST_BUILDS_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    print(response.json())


def retrieve(self, dapp_slug, id):
    uri = RETRIEVE_BUILD_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.get(uri=uri)
    print(response.json())
