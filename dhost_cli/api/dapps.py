LIST_DAPPS_URL = 'v1/dapps/'
RETRIEVE_DAPP_URL = 'v1/dapps/{dapp_slug}/'


def list(self):
    uri = LIST_DAPPS_URL
    response = self.get(uri=uri)
    title = 'Listing your dapps'
    print_dapp(response.json(), many=True, title=title)


def retrieve(self, dapp_slug):
    """Get details about a dapp."""
    uri = RETRIEVE_DAPP_URL.format(dapp_slug=dapp_slug)
    response = self.get(uri=uri)
    title = f'Details for dapp: {dapp_slug}'
    print_dapp(response.json(), title=title)


def print_dapp(data, many=False, title=None):
    if title:
        print(title)
    if many:
        return _print_many_dapp(data)
    return _print_single_dapp(data)


def _print_single_dapp(dapp):
    print()
    print('Dapp: {}'.format(dapp['slug']))
    print('  * Status: {}'.format(dapp['status']))
    print('  * Type: {}'.format(dapp['dapp_type']))

    if dapp['url']:
        print('URL: {}'.format(dapp['url']))


def _print_many_dapp(dapp_list):
    for dapp in dapp_list:
        _print_single_dapp(dapp)
