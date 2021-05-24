from .dhost_cli import DhostAPI
from .utils import get_user_str_input


class IPFSDappManagement(DhostAPI):
    def list(self):
        print('Listing your IPFS dapps')
        uri = 'ipfs/'
        response = self.get(uri=uri)
        self._print_many_dapp(response.json())

    def read(self, dapp_id):
        """Get details about an IPFs dapp."""
        print('Details for IPFS dapp: {}'.format(dapp_id))
        uri = 'ipfs/' + dapp_id
        response = self.get(uri=uri)
        self._print_single_dapp(response.json())

    def update(self, dapp_id, *args, **kwargs):
        """Update an IPFS dapp"""
        print('Updating IPFS dapp: {}'.format(dapp_id))
        uri = 'ipfs/' + dapp_id
        response = self.put(uri=uri, data=kwargs)
        self._print_single_dapp(response.json())

    def create(self, name=None, command=None, docker=None, slug=None):
        """Create an IPFS dapp"""
        uri = 'ipfs/'

        name = get_user_str_input(name, 'IPFS dapp name')
        command = get_user_str_input(command, 'Build command')
        docker = get_user_str_input(docker, 'Docker image')
        slug = get_user_str_input(slug, 'Slug')

        data = {
            'name': name,
            'command': command,
            'docker': docker,
            'slug': slug,
        }

        response = self.post(uri=uri, data=data)

        if response.status_code == 201:
            print("Successfuly created IPFS dapp: '{}'.".format(name))
            self._print_single_dapp(response.json())
        else:
            print('Error while creating dapp {}.'.format(response.status_code))
            print(response.json())

    def delete(self, dapp_id):
        """Delete an IPFS dapp"""
        print('Deleting IPFS dapp: {}'.format(dapp_id))
        uri = 'ipfs/' + dapp_id
        r = self.delete(uri=uri)
        print(r.content)

    def build(self, dapp_id):
        """Build an IPFS dapp"""
        print('Building IPFS dapp: {}'.format(dapp_id))

    def deploy(self, dapp_id):
        """Deploy and IPFS dapp"""
        print('Deploying IPFS dapp: {}'.format(dapp_id))

    @classmethod
    def _print_response(cls, response):
        print(response)

    @classmethod
    def _print_single_dapp(cls, dapp, index=None):
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

    @classmethod
    def _print_many_dapp(cls, dapp_list):
        for index, dapp in enumerate(dapp_list, start=1):
            print()
            cls._print_single_dapp(dapp, index)
