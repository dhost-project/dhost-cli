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


def create(self, name=None, command=None, docker=None, slug=None):
    """Create an IPFS dapp"""
    uri = CREATE_DAPP_URL
    name = get_user_str_input(name, 'IPFS dapp name')
    data = {
        'name': name,
        'command': get_user_str_input(command, 'Build command'),
        'docker': get_user_str_input(docker, 'Docker image'),
        'slug': get_user_str_input(slug, 'Slug'),
    }
    response = self.post(uri=uri, data=data)
    print(f"Successfuly created IPFS dapp: '{slug}'.")
    print_dapp(response.json())


def destroy(self, dapp_slug):
    """Delete an IPFS dapp"""
    uri = DELETE_DAPP_URL.format(dapp_slug=dapp_slug)
    r = self.delete(uri=uri)
    print(f'Deleting IPFS dapp: {dapp_slug}')
    print(r.content)


def build(self, dapp_slug):
    """Build an IPFS dapp"""
    uri = BUILD_DAPP_URL.format(dapp_slug=dapp_slug)
    r = self.get(uri=uri)
    print(f'Building IPFS dapp: {dapp_slug}')
    print(r.content)


def deploy(self, dapp_slug):
    """Deploy and IPFS dapp"""
    uri = DEPLOY_DAPP_URL.format(dapp_slug=dapp_slug)
    r = self.get(uri=uri)
    print(f'Deploying IPFS dapp {dapp_slug}')
    print(r.content)


def print_dapp(dapp, many=False, *args, **kwargs):
    if many:
        return _print_many_dapp(dapp, *args, **kwargs)
    else:
        return _print_single_dapp(dapp, *args, **kwargs)


def _print_single_dapp(dapp, index=None):
    if index is None:
        if 'id' in dapp:
            index = dapp['id']
        else:
            index = dapp['name']
    print('____ Dapp [{}] '.format(index) + '_' * 15)
    print('{}'.format(dapp['slug']))
    print('Status: {}'.format(dapp['status']))

    if dapp['url']:
        print('URL: {}'.format(dapp['url']))

    print('Build command: {}'.format(dapp['command']))
    print('Docker: {}'.format(dapp['docker']))

    builds_number = len(dapp['builds'])
    if builds_number:
        print('Number of builds: {}'.format(builds_number))

    bundles_number = len(dapp['bundles'])
    if bundles_number:
        print('Number of bundles: {}'.format(bundles_number))

    deployments_number = len(dapp['deployments'])
    if deployments_number:
        print('Number of deployments: {}'.format(deployments_number))


def _print_many_dapp(dapp_list):
    for index, dapp in enumerate(dapp_list, start=1):
        print()
        _print_single_dapp(dapp, index)
