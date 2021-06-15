LIST_ENVVARS_URL = 'v1/ipfs/{dapp_slug}/envvars/'
CREATE_ENVVAR_URL = 'v1/ipfs/{dapp_slug}/envvars/'
RETRIEVE_ENVVAR_URL = 'v1/ipfs/{dapp_slug}/envvars/{id}/'
UPDATE_ENVVAR_URL = 'v1/ipfs/{dapp_slug}/envvars/{id}/'
PARTIAL_UPDATE_ENVVAR_URL = 'v1/ipfs/{dapp_slug}/envvars/{id}/'
DESTROY_ENVVAR_URL = 'v1/ipfs/{dapp_slug}/envvars/{id}/'


def list(self, dapp_slug):
    uri = LIST_ENVVARS_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    print(response.json())


def create(self, dapp_slug, **data):
    uri = CREATE_ENVVAR_URL.format(dapp_slug=dapp_slug)
    response = self.post(uri=uri, data=data)
    print(response.json())


def retrieve(self, dapp_slug, id):
    uri = RETRIEVE_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.get(uri=uri)
    print(response.json())


def update(self, dapp_slug, id, **data):
    uri = UPDATE_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.post(uri=uri, data=data)
    print(response.json())


def partial_update(self, dapp_slug, id, **data):
    uri = PARTIAL_UPDATE_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.patch(uri=uri, data=data)
    print(response.json())


def destroy(self, dapp_slug, id):
    uri = DESTROY_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.delete(uri=uri)
    print(response.json())
