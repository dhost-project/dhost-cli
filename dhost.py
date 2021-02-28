#!/usr/bin/python3

import argparse
import requests
from getpass import getpass


DEFAULT_API_URL = 'http://127.0.0.1:8000/'
TOKEN_AUTH_URL = 'token-auth/'
TOKEN_PREFIX = 'Token'


class DhostAPI:
    """A common class to call the Dhost API,
    You should subclass this to implement call to the API."""

    def __init__(
        self,
        token=None,
        username=None,
        API_URL=DEFAULT_API_URL,
        TOKEN_AUTH_URL = TOKEN_AUTH_URL,
        TOKEN_PREFIX=TOKEN_PREFIX,
    ):
        self.username = username
        self.token = token
        self.API_URL = API_URL
        self.TOKEN_AUTH_URL = TOKEN_AUTH_URL
        self.TOKEN_PREFIX = TOKEN_PREFIX

        if self.token is None:
            self.authentify()

    def authentify(self):
        if self.username is None:
            self.username = input('username: ')
        self.get_token_auth()

    def get_token_auth(self):
        url = self.API_URL + self.TOKEN_AUTH_URL
        password = getpass('password: ')
        cred = {'username': self.username, 'password': password}
        r = requests.post(url, data=cred)
        if r.status_code == 200:
            self.token = r.json()['token']
            return self.token
        else:
            print('Authentication failure, code:', r.status_code)

    def get_token(self):
        return self.token

    def _get_authorization_header(self, token=None):
        """Use the passed token if available"""
        token = self.token if token is None else token
        return {'Authorization': self.TOKEN_PREFIX + ' ' + token}

    def _prepare_api_request(self, uri=None, url=None, headers=None):
        """Prepare and API request with authorization header and build URL"""
        if url is None:
            if uri is None:
                raise Exception('You must provide either an URL or an URI to make an API request.')
            else:
                url = self.API_URL + uri
        # TODO add passed headers params
        headers = self._get_authorization_header(token=token)
        return url, headers

    def post(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a POST request to the API"""
        url, headers = self._prepare_api_request(url=url, uri=uri, headers=headers)
        return requests.post(url, headers=headers, *args, **kwargs)

    def get(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a GET request to the API"""
        url, headers = self._prepare_api_request(url=url, uri=uri, headers=headers)
        return requests.get(url, headers=headers, *args, **kwargs)

    def put(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a PUT request to the API"""
        url, headers = self._prepare_api_request(url=url, uri=uri, headers=headers)
        return requests.put(url, headers=headers, *args, **kwargs)

    def patch(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a PUT request to the API"""
        url, headers = self._prepare_api_request(url=url, uri=uri, headers=headers)
        return requests.patch(url, headers=headers, *args, **kwargs)

    def delete(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a DELETE request to the API"""
        url, headers = self._prepare_api_request(url=url, uri=uri, headers=headers)
        return requests.delete(url, headers=headers, *args, **kwargs)

    def head(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a HEAD request to the API"""
        url, headers = self._prepare_api_request(url=url, uri=uri, headers=headers)
        return requests.head(url, *args, **kwargs)

    def post_file(self, file_paht, *args, **kwargs):
        # TODO get file here
        file = ''
        return self.post(file=file, *args, **kwargs)


class AppManagement(DhostAPI):
    def list_apps(self):
        print('listing apps')
        uri = 'apps/'
        # r = self.get(uri=uri)
        # print(r)

    def read_app(self, app_name):
        """Get details about an app."""
        print('details for app: ' + app_name)
        uri = 'apps/' + app_name
        # r = self.get(uri=uri)
        # print(r)

    def update_app(self, app_name, *args, **kwargs):
        """Update an app"""
        print('updating app: ' + app_name)
        uri = 'apps/' + app_name
        # r = self.put(uri=uri, data=kwargs)
        # print(r)

    def create_app(self, app_name):
        """Create an app"""
        print('creating app: ' + app_name)
        uri = 'apps/'
        data = {'name': app_name}
        # r = self.post(uri=uri, data=data)
        # print(r)

    def delete_app(self, app_name):
        """Delete an app"""
        print('deleting app: ' + app_name)
        uri = 'apps/' + app_name
        # r = self.delete(uri=uri)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='dhost', description='%(prog)s CLI tool to host decentralized websites.')

    parser.add_argument('-u', '--username', help="Connect to API with username and password.")
    parser.add_argument('-t', '--token', help="Connect to API with token.")
    parser.add_argument('-T', '--get-token', action='store_true', help="Get your API token from username and password.")
    parser.add_argument('-a', '--api_url', default=DEFAULT_API_URL)
    #parser.add_argument('INPUT_FILE', help='file to upload', type=argparse.FileType('r'), default=sys.stdin)

    subparser = parser.add_subparsers(dest='cmd')

    app = subparser.add_parser('app', help="Manage you apps")
    app_sub = app.add_subparsers(dest='app_cmd')

    # app list
    list_app = app_sub.add_parser('list', help="List apps.")

    # app create
    create_app = app_sub.add_parser('create', help="Create a new app.")
    create_app.add_argument('app_name')

    # app infos
    detail_app = app_sub.add_parser('infos', help="Get details about and app.")
    detail_app.add_argument('app_name')

    # app update
    update_app = app_sub.add_parser('update', help="Update and app.")
    update_app.add_argument('app_name')

    # app delete
    delete_app = app_sub.add_parser('delete', help="Delete an app.")
    delete_app.add_argument('app_name')

    args = parser.parse_args()


    if args.get_token:
        print('Token: ' + instance.get_token())

    if args.cmd is None:
        instance = DhostAPI(
            token=args.token,
            username=args.username,
            API_URL=args.api_url,
        )
    elif args.cmd=='app':
        app_cmd = args.app_cmd
        instance = AppManagement(
            token=args.token,
            username=args.username,
            API_URL=args.api_url,
        )
        if app_cmd=='list':
            instance.list_apps()
        elif app_cmd=='infos':
            instance.read_app(args.app_name)
        elif app_cmd=='update':
            instance.update_app(args.app_name)
        elif app_cmd=='create':
            instance.create_app(args.app_name)
        elif app_cmd=='delete':
            instance.delete_app(args.app_name)

