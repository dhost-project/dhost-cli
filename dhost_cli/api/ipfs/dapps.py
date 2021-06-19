from dhost_cli.utils import get_user_str_input

LIST_DAPPS_URL = 'v1/ipfs/'
CREATE_DAPP_URL = 'v1/ipfs/'
RETRIEVE_DAPP_URL = 'v1/ipfs/{dapp_slug}/'
UPDATE_DAPP_URL = 'v1/ipfs/{dapp_slug}/'
PARTIAL_UPDATE_DAPP_URL = 'v1/ipfs/{dapp_slug}/'
DELETE_DAPP_URL = 'v1/ipfs/{dapp_slug}/'
BUILD_DAPP_URL = 'v1/ipfs/{dapp_slug}/build'
DEPLOY_DAPP_URL = 'v1/ipfs/{dapp_slug}/deploy'


def list(self):
    response = self.get(uri=LIST_DAPPS_URL)
    print('Listing your IPFS dapps')
    print_dapp(response.json(), many=True)


def retrieve(self, dapp_slug):
    """Get details about an IPFs dapp."""
    uri = RETRIEVE_DAPP_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    print('Details for IPFS dapp {}'.format(dapp_slug))
    print_dapp(response.json())


def update(self, dapp_slug, *args, **kwargs):
    """Update an IPFS dapp"""
    uri = UPDATE_DAPP_URL.format(dapp_slug=dapp_slug)
    response = self.put(uri=uri, data=kwargs)
    print('Updating IPFS dapp: {}'.format(dapp_slug))
    print_dapp(response.json())


def partial_update(self, dapp_slug, **data):
    uri = PARTIAL_UPDATE_DAPP_URL.format(dapp_slug=dapp_slug)
    response = self.patch(uri=uri, data=data)
    print('Partial update IPFS dapp: {}'.format(dapp_slug))
    print_dapp(response.json())


def create(self, slug=None):
    """Create an IPFS dapp"""
    uri = CREATE_DAPP_URL
    slug = get_user_str_input(slug, 'slug')
    data = {
        'slug': slug,
    }
    response = self.post(uri=uri, data=data)
    print(f"Successfuly created IPFS dapp: '{slug}'.")
    print_dapp(response.json())


def destroy(self, dapp_slug):
    """Delete an IPFS dapp"""
    uri = DELETE_DAPP_URL.format(dapp_slug=dapp_slug)
    self.delete(uri=uri)
    print(f'Successfuly deleted IPFS dapp: {dapp_slug}')


def deploy(self, dapp_slug):
    """Deploy and IPFS dapp"""
    uri = DEPLOY_DAPP_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    status = response.json()['status']
    print(f'IPFS dapp {dapp_slug}: {status}')


def print_dapp(data, many=False, title=None):
    if title:
        print(title)
    if many:
        return _print_many_dapp(data)
    return _print_single_dapp(data)


def _print_single_dapp(dapp):
    print()
    print('Dapp: {}'.format(dapp['slug']))
    print('  * IPFS hash: {}'.format(dapp['ipfs_hash']))
    print('  * IPFS gateway: {}'.format(dapp['ipfs_gateway']))
    if dapp['url']:
        print('URL: {}'.format(dapp['url']))
    print('  * Status: {}'.format(dapp['status']))
    print('  * Created at: {}'.format(dapp['created_at']))


def _print_many_dapp(dapp_list):
    for dapp in dapp_list:
        _print_single_dapp(dapp)
