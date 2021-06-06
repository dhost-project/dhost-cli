"""Main module."""

import datetime
from getpass import getpass

import requests

from dhost_cli import settings
from dhost_cli.db import (fetch_all_tokens, fetch_token, init_database,
                          save_token)


class Client:

    API_URL = settings.DEFAULT_API_URL
    TOKEN_PREFIX = settings.TOKEN_PREFIX
    OAUTH_SERVER_URL = settings.OAUTH_SERVER_URL
    OAUTH_TOKEN_URL = settings.OAUTH_TOKEN_URL
    OAUTH_CLIENT_ID = settings.OAUTH_CLIENT_ID

    def __init__(
        self,
        token=None,
        username=None,
        password=None,
    ):
        self.username = username
        self.password = password
        self.token = token if token else self.get_token_or_authentify()

    def get_token_or_authentify(self):
        """Get the token from the database if it exist, or authentify user"""
        init_database()
        now = datetime.datetime.now() - datetime.timedelta(seconds=120)
        access_token, refresh_token, expires = fetch_token()

        if expires:
            expires_at = datetime.datetime.strptime(expires,
                                                    "%Y-%m-%d %H:%M:%S.%f")
            if expires_at < now:
                access_token, refresh_token, expires = self._send_refresh_token(
                    refresh_token)
                save_token(access_token, refresh_token, expires)

        if access_token is None:
            access_token, refresh_token, expires_in = self.authentify()
            expires = now + datetime.timedelta(seconds=expires_in)
            save_token(access_token, refresh_token, expires)
        return access_token

    def authentify(self):
        """
        With the `Resource owner password-based` on a public client type
        this function will authenticate the user from his credentials and get
        a token to access the API
        """
        if self.username:
            username = self.username
        else:
            username = input('username: ')

        # Give the user 3 attempt to give the correct password
        for retry in range(0, 3):
            if self.password:
                password = self.password
            else:
                password = getpass('password: ')
            try:
                access_token, refresh_token, expires_in = self._get_token_oauth(
                    username=username, password=password)
                if access_token:
                    return access_token, refresh_token, expires_in
            except Exception as e:
                print(e)

        raise Exception('Failed to authentify.')

    @classmethod
    def _get_token_oauth(cls, username, password):
        url = cls.OAUTH_SERVER_URL + cls.OAUTH_TOKEN_URL
        cred = {
            'username': username,
            'password': password,
            'client_id': cls.OAUTH_CLIENT_ID,
            'grant_type': 'password'
        }
        r = requests.post(url, data=cred)
        if r.status_code == 200:
            access_token = r.json()['access_token']
            refresh_token = r.json()['refresh_token']
            expires_in = r.json()['expires_in']
            return access_token, refresh_token, expires_in
        else:
            if 'error_description' in r.json():
                raise Exception(r.json()['error_description'])
            else:
                raise Exception(
                    'Failed to authentify with credentials given. Code: {}'
                    '\nMessage: {}.'.format(r.status_code, r.json()))

    @classmethod
    def _send_refresh_token(cls, refresh_token):
        """Send a request to the OAuth server to refresh the passed token"""
        url = cls.OAUTH_SERVER_URL + cls.OAUTH_TOKEN_URL
        cred = {
            'refresh_token': refresh_token,
            'client_id': cls.OAUTH_CLIENT_ID,
            'grant_type': 'refresh_token',
        }
        r = requests.post(url, data=cred)
        if r.status_code == 200:
            access_token = r.json()['access_token']
            refresh_token = r.json()['refresh_token']
            expires_in = r.json()['expires_in']
            return access_token, refresh_token, expires_in
        else:
            raise Exception(
                'Failed to refresh token. Code: {}\nMessage: {}.'.format(
                    r.status_code, r.json()))

    def refresh_token(self, token_id):
        print('Refreshing token {}.'.format(token_id))

    def get_token(self):
        return self.token

    def _get_authorization_header(self, token=None):
        """Use the passed token if available"""
        token = self.token if token is None else token
        return {'Authorization': self.TOKEN_PREFIX + ' ' + token}

    def _prepare_api_request(self,
                             uri=None,
                             url=None,
                             headers=None,
                             token=None):
        """Prepare and API request with authorization header and build URL"""
        if url is None:
            if uri is None:
                raise Exception(
                    'You must provide either an URL or an URI to make an API '
                    'request.')
            else:
                url = self.API_URL + uri
        # TODO add passed headers params
        headers = self._get_authorization_header(token=token)
        return url, headers

    def list_tokens(self):
        token_list = fetch_all_tokens()
        for index, tokens in enumerate(token_list, start=1):
            print("_ [{}]".format(index), "_" * 10)
            print("Token: {}".format(tokens[0]))
            print("Refresh token: {}".format(tokens[1]))

    def revoke_token(self, token_id):
        print(token_id)

    def post(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a POST request to the API"""
        url, headers = self._prepare_api_request(url=url,
                                                 uri=uri,
                                                 headers=headers)
        return requests.post(url, headers=headers, *args, **kwargs)

    def get(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a GET request to the API"""
        url, headers = self._prepare_api_request(url=url,
                                                 uri=uri,
                                                 headers=headers)
        response = requests.get(url, headers=headers, *args, **kwargs)
        if response.status_code == 200:
            return response
        else:
            raise Exception('Error {}\n{}'.format(response.status_code,
                                                  response.content))

    def put(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a PUT request to the API"""
        url, headers = self._prepare_api_request(url=url,
                                                 uri=uri,
                                                 headers=headers)
        response = requests.put(url, headers=headers, *args, **kwargs)
        return response

    def patch(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a PUT request to the API"""
        url, headers = self._prepare_api_request(url=url,
                                                 uri=uri,
                                                 headers=headers)
        response = requests.patch(url, headers=headers, *args, **kwargs)
        return response

    def delete(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a DELETE request to the API"""
        url, headers = self._prepare_api_request(url=url,
                                                 uri=uri,
                                                 headers=headers)
        response = requests.delete(url, headers=headers, *args, **kwargs)
        return response

    def head(self, uri=None, url=None, headers=None, *args, **kwargs):
        """Send a HEAD request to the API"""
        url, headers = self._prepare_api_request(url=url,
                                                 uri=uri,
                                                 headers=headers)
        response = requests.head(url, *args, **kwargs)
        return response

    def post_file(self, file_paht, *args, **kwargs):
        # TODO get file here
        file = ''
        response = self.post(file=file, *args, **kwargs)
        return response


from dhost_cli.api import github, ipfs, users


def call_wrapper(function):
    def wrap(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrap


Client.github_list = call_wrapper(github.list)
Client.github_fetch_all = call_wrapper(github.fetch_all)
Client.github_retrieve = call_wrapper(github.retrieve)
Client.github_fetch_repo = call_wrapper(github.fetch_repo)
Client.ipfs_list = call_wrapper(ipfs.list)
Client.ipfs_read = call_wrapper(ipfs.read)
Client.ipfs_update = call_wrapper(ipfs.update)
Client.ipfs_create = call_wrapper(ipfs.create)
Client.ipfs_delete = call_wrapper(ipfs.delete)
Client.ipfs_build = call_wrapper(ipfs.build)
Client.ipfs_deploy = call_wrapper(ipfs.deploy)
Client.users_me = call_wrapper(users.me)
