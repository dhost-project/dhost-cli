from dhost_cli.api.utils import basic_print

LIST_ENVVARS_URL = "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/envvars/"
CREATE_ENVVAR_URL = "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/envvars/"
RETRIEVE_ENVVAR_URL = "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/envvars/{id}/"
UPDATE_ENVVAR_URL = "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/envvars/{id}/"
PARTIAL_UPDATE_ENVVAR_URL = (
    "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/envvars/{id}/"
)
DESTROY_ENVVAR_URL = "ipfs/{dapp_slug}/buildoptions/{dapp_slug}/envvars/{id}/"


def list(self, dapp_slug):
    uri = LIST_ENVVARS_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    basic_print(response.json(), many=True)


def create(self, dapp_slug, **data):
    uri = CREATE_ENVVAR_URL.format(dapp_slug=dapp_slug)
    response = self.post(uri=uri, data=data)
    basic_print(response.json())


def retrieve(self, dapp_slug, id):
    uri = RETRIEVE_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.get(uri=uri)
    basic_print(response.json())


def update(self, dapp_slug, id, **data):
    uri = UPDATE_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.post(uri=uri, data=data)
    basic_print(response.json())


def partial_update(self, dapp_slug, id, **data):
    uri = PARTIAL_UPDATE_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    response = self.patch(uri=uri, data=data)
    basic_print(response.json())


def destroy(self, dapp_slug, id):
    uri = DESTROY_ENVVAR_URL.format(dapp_slug=dapp_slug, id=id)
    self.delete(uri=uri)
    print("Successfuly deleted env var with id: {id}.".format(id=id))
