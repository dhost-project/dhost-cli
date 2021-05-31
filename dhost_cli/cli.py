#!/usr/bin/env python
#  ____  _   _           _         ____ _     ___
# |  _ \| | | | ___  ___| |_      / ___| |   |_ _|
# | | | | |_| |/ _ \/ __| __|____| |   | |    | |
# | |_| |  _  | (_) \__ \ ||_____| |___| |___ | |
# |____/|_| |_|\___/|___/\__|     \____|_____|___|
#
# Command-line interface script for dhost.
#

import argparse
import sys

from dhost_cli import settings
from dhost_cli.dhost_cli import DhostAPI
from dhost_cli.ipfs_dapp_api import IPFSDappManagement
from dhost_cli.github_api import GithubManagement
from dhost_cli.user_api import UserManagement


def main():
    parser = argparse.ArgumentParser(
        prog='dhost',
        description='%(prog)s CLI tool to host decentralized websites.',
    )

    parser.add_argument('-u',
                        '--username',
                        help="Connect to API with username and password.")
    parser.add_argument('-t', '--token', help="Connect to API with token.")
    parser.add_argument('-T',
                        '--get-token',
                        action='store_true',
                        help="Get your API token from username and password.")
    parser.add_argument('-a', '--api-url', default=settings.DEFAULT_API_URL)

    subparser = parser.add_subparsers(dest='cmd')

    token = subparser.add_parser('token', help="Manage your API tokens.")
    token_sub = token.add_subparsers(dest='token_cmd')
    token_sub.add_parser('list', help="List your API tokens.")
    revoke_token = token_sub.add_parser('revoke', help="Revoke API token.")
    revoke_token.add_argument('token_id', help="The token id from `list`.")
    refresh_token = token_sub.add_parser('refresh', help="Refresh API token.")
    refresh_token.add_argument('token_id', help="The token id from `list`.")

    user = subparser.add_parser('user', help="Manage your infos.")

    ipfs_dapp = subparser.add_parser('ipfs', help="Manage your IPFS dapps.")
    ipfs_dapp_sub = ipfs_dapp.add_subparsers(dest='ipfs_dapp_cmd')
    ipfs_dapp_sub.add_parser('list', help="List IPFS dapps.")

    create_ipfs_dapp = ipfs_dapp_sub.add_parser('create',
                                                help="Create a new IPFS dapp.")
    create_ipfs_dapp.add_argument('-n', '--dapp-name')
    create_ipfs_dapp.add_argument('-b', '--build-command')
    create_ipfs_dapp.add_argument('-d', '--docker')
    create_ipfs_dapp.add_argument('-s', '--slug')

    detail_ipfs_dapp = ipfs_dapp_sub.add_parser(
        'infos', help="Get details about an IPFS dapps.")
    detail_ipfs_dapp.add_argument('ipfs_dapp_id')

    update_ipfs_dapp = ipfs_dapp_sub.add_parser('update',
                                                help="Update an IPFS dapp.")
    update_ipfs_dapp.add_argument('IPFS-dapp-id')
    update_ipfs_dapp.add_argument('-n', '--dapp-name', help="New dapp name.")
    update_ipfs_dapp.add_argument('-b',
                                  '--build-command',
                                  help="New dapp build command.")
    update_ipfs_dapp.add_argument('-d', '--docker', help="New dapp docker.")
    update_ipfs_dapp.add_argument('-s', '--slug', help="New dapp slug.")

    delete_ipfs_dapp = ipfs_dapp_sub.add_parser('delete',
                                                help="Delete an IPFS dapp.")
    delete_ipfs_dapp.add_argument('ipfs_dapp_id')

    github = subparser.add_parser('github', help="Manage your github repos.")
    github_sub = github.add_subparsers(dest='github_cmd')
    github_sub.add_parser('list')
    github_sub.add_parser('me')
    github_sub.add_parser('scopes')

    args = parser.parse_args()

    if args.get_token:
        instance = DhostAPI(
            token=args.token,
            username=args.username,
            API_URL=args.api_url,
        )
        print('Token: ' + instance.get_token())
        return 0

    if args.cmd == 'token':
        instance = DhostAPI(
            token=args.token,
            username=args.username,
            API_URL=args.api_url,
        )
        if args.token_cmd == 'list':
            instance.list_tokens()
        elif args.token_cmd == 'revoke':
            instance.revoke_token(args.token_id)
        elif args.token_cmd == 'refresh_token':
            instance.refresh_token(args.token_id)
    elif args.cmd == 'user':
        instance = UserManagement(
            token=args.token,
            username=args.username,
            API_URL=args.api_url,
        )
        instance.read()
    elif args.cmd == 'ipfs':
        ipfs_dapp_cmd = args.ipfs_dapp_cmd
        instance = IPFSDappManagement(
            token=args.token,
            username=args.username,
            API_URL=args.api_url,
        )
        if ipfs_dapp_cmd == 'list':
            instance.list()
        elif ipfs_dapp_cmd == 'infos':
            instance.read(args.ipfs_dapp_id)
        elif ipfs_dapp_cmd == 'update':
            instance.update(args.ipfs_dapp_id)
        elif ipfs_dapp_cmd == 'create':
            instance.create(
                args.dapp_name,
                args.build_command,
                args.docker,
                args.slug,
            )
        elif ipfs_dapp_cmd == 'delete':
            instance.delete(args.ipfs_dapp_id)
    elif args.cmd == 'github':
        instance = GithubManagement(
            token=args.token,
            username=args.username,
            API_URL=args.api_url,
        )
        if args.github_cmd == 'list':
            instance.list()
        elif args.github_cmd == 'me':
            instance.me()
        elif args.github_cmd == 'scopes':
            instance.scopes()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
