"""Main module."""

import datetime
from getpass import getpass

import requests

from dhost_cli import settings
from dhost_cli.db import fetch_token, init_database, save_token


class DhostAPI:
    """
    A common class to call the Dhost API,
    You should subclass this to implement call to the API.
    """
    def __init__(
        self,
        token=None,
        username=None,
        OAUTH_SERVER_URL=settings.OAUTH_SERVER_URL,
        OAUTH_TOKEN_URL=settings.OAUTH_TOKEN_URL,
        OAUTH_CLIENT_ID=settings.OAUTH_CLIENT_ID,
        TOKEN_PREFIX=settings.TOKEN_PREFIX,
        API_URL=settings.DEFAULT_API_URL,
    ):
        self.OAUTH_SERVER_URL = OAUTH_SERVER_URL
        self.OAUTH_TOKEN_URL = OAUTH_TOKEN_URL
        self.OAUTH_CLIENT_ID = OAUTH_CLIENT_ID
        self.TOKEN_PREFIX = TOKEN_PREFIX
        self.API_URL = API_URL

        self.username = username
        self.token = token if token else self.get_token_or_authentify()

    def get_token_or_authentify(self):
        """Get the token from the database if it exist, or authentify user"""
        init_database()
        now = datetime.datetime.now() - datetime.timedelta(seconds=120)
        access_token, refresh_token, expires = fetch_token()

        if expires:
            expires = datetime.datetime.strptime(expires,
                                                 "%Y-%m-%d %H:%M:%S.%f")
            if expires < now:
                access_token, refresh_token, expires = self.refresh_token(
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
        url = self.OAUTH_SERVER_URL + self.OAUTH_TOKEN_URL
        if self.username is None:
            self.username = input('username: ')
        password = getpass('password: ')
        cred = {
            'username': self.username,
            'password': password,
            'client_id': self.OAUTH_CLIENT_ID,
            'grant_type': 'password'
        }
        r = requests.post(url, data=cred)
        if r.status_code == 200:
            access_token = r.json()['access_token']
            refresh_token = r.json()['refresh_token']
            expires_in = r.json()['expires_in']
            return access_token, refresh_token, expires_in
        else:
            print('Authentication failure, code:', r.status_code)
            print(r.json())

    def refresh_token(self, refresh_token):
        url = self.OAUTH_SERVER_URL + self.OAUTH_TOKEN_URL
        cred = {
            'refresh_token': refresh_token,
            'client_id': self.OAUTH_CLIENT_ID,
            'grant_type': 'refresh_token',
        }
        r = requests.post(url, data=cred)
        if r.status_code == 200:
            access_token = r.json()['access_token']
            refresh_token = r.json()['refresh_token']
            expires_in = r.json()['expires_in']
            return access_token, refresh_token, expires_in
        else:
            print('Refresh token failure, code:', r.status_code)
            print(r.json())

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
            print('Message:\n{}'.format(response.content))
            raise Exception('Error {}'.format(response.status_code))

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
