from .dhost_cli import DhostAPI
from .utils import get_user_str_input


class IPFSDappManagement(DhostAPI):
    def list(self):
        print('Listing your IPFS dapps')
        uri = 'ipfs/'
        response = self.get(uri=uri)
        print(response.content)

    def read(self, dapp_id):
        """Get details about an IPFs dapp."""
        print('Details for IPFS dapp: ' + dapp_id)
        uri = 'ipfs/' + dapp_id
        r = self.get(uri=uri)
        print(r.content)

    def update(self, dapp_id, *args, **kwargs):
        """Update an IPFS dapp"""
        print('Updating IPFS dapp: ' + dapp_id)
        uri = 'ipfs/' + dapp_id
        r = self.put(uri=uri, data=kwargs)
        print(r.content)

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

        print('Creating IPFS dapp: `{}`'.format(name))
        response = self.post(uri=uri, data=data)
        print(response.content)

    def delete(self, dapp_id):
        """Delete an IPFS dapp"""
        print('Deleting IPFS dapp: ' + dapp_id)
        uri = 'ipfs/' + dapp_id
        r = self.delete(uri=uri)
        print(r.content)
