LIST_DAPPS_URL = 'v1/dapps/'
RETRIEVE_DAPP_URL = 'v1/dapps/{dapp_slug}/'


def list(self):
    uri = LIST_DAPPS_URL
    response = self.get(uri=uri)
    print('Listing your dapps')
    print_dapp(response.json(), many=True)


def read(self, dapp_slug):
    """Get details about an IPFs dapp."""
    uri = RETRIEVE_DAPP_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    print(f'Details for IPFS dapp: {dapp_slug}')
    print_dapp(response.json(), many=False)


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
    print('{} [{}]'.format(dapp['name'], dapp['id']))
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
