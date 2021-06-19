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

from dhost_cli import __version__
from dhost_cli.api.client import Client


def main():
    parser = argparse.ArgumentParser(
        prog='dhost',
        description='%(prog)s CLI tool to host decentralized websites.',
    )

    parser.add_argument('-v', '--version', action='store_true')
    parser.add_argument('-u',
                        '--username',
                        help="Connect to API with username and password.")
    parser.add_argument('-p',
                        '--password',
                        help="Connect to API with username and password.")
    parser.add_argument('-t', '--token', help="Connect to API with token.")
    parser.add_argument('-T',
                        '--get-token',
                        action='store_true',
                        help="Get your API token from username and password.")
    parser.add_argument('--raise-exceptions',
                        action='store_true',
                        help="Raise exceptions instead of just printing them.")
    parser.add_argument('--disable-color',
                        action='store_true',
                        help="Disable colored output.")

    subparser = parser.add_subparsers(dest='cmd')

    token = subparser.add_parser('token', help="Manage your API tokens.")
    token_sub = token.add_subparsers(dest='token_cmd')
    token_sub.add_parser('list', help="List your API tokens.")
    revoke_token = token_sub.add_parser('revoke', help="Revoke API token.")
    revoke_token.add_argument('token_id', help="The token id from `list`.")
    refresh_token = token_sub.add_parser('refresh', help="Refresh API token.")
    refresh_token.add_argument('token_id', help="The token id from `list`.")

    subparser.add_parser('me', help="Manage your infos.")

    ipfs_dapp = subparser.add_parser('ipfs', help="Manage your IPFS dapps.")
    ipfs_dapp_sub = ipfs_dapp.add_subparsers(dest='ipfs_dapp_cmd')
    ipfs_dapp_sub.add_parser('list', help="List IPFS dapps.")

    create_ipfs_dapp = ipfs_dapp_sub.add_parser('create',
                                                help="Create a new IPFS dapp.")
    create_ipfs_dapp.add_argument('-n', '--dapp-name')
    create_ipfs_dapp.add_argument('-b', '--build-command')
    create_ipfs_dapp.add_argument('-d', '--docker')
    create_ipfs_dapp.add_argument('-s', '--slug')

    detail_ipfs_dapp = ipfs_dapp_sub.add_parser('ret',
                                                help="Retrieve an IPFS dapps.")
    detail_ipfs_dapp.add_argument('ipfs_dapp_slug')

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
    delete_ipfs_dapp.add_argument('ipfs_dapp_slug')

    github = subparser.add_parser('github', help="Manage your github repos.")
    github_sub = github.add_subparsers(dest='github_cmd')
    github_sub.add_parser('list')
    read_github = github_sub.add_parser('read')
    read_github.add_argument('repo')
    read_github = github_sub.add_parser('fetch')
    read_github.add_argument('repo', nargs="?")

    dispatch(parser)

    return 0


def dispatch(parser):
    args = parser.parse_args()

    client = Client(
        token=args.token,
        username=args.username,
        password=args.password,
        raise_exceptions=args.raise_exceptions,
        color=not args.disable_color,
    )

    if args.version:
        print('dhost-cli version {}'.format(__version__))
    elif args.get_token:
        print('Token: ' + client.get_token())

    elif args.cmd == 'token':
        if args.token_cmd == 'list':
            client.list_tokens()
        elif args.token_cmd == 'revoke':
            client.revoke_token(args.token_id)
        elif args.token_cmd == 'refresh_token':
            client.refresh_token(args.token_id)

    elif args.cmd == 'me':
        client.users_me()

    elif args.cmd == 'ipfs':
        if args.ipfs_dapp_cmd == 'list':
            client.ipfs_list()
        elif args.ipfs_dapp_cmd == 'ret':
            client.ipfs_retrieve(args.ipfs_dapp_slug)
        elif args.ipfs_dapp_cmd == 'update':
            client.ipfs_update(args.ipfs_dapp_slug)
        elif args.ipfs_dapp_cmd == 'create':
            client.ipfs_create(
                args.dapp_name,
                args.build_command,
                args.docker,
                args.slug,
            )
        elif args.ipfs_dapp_cmd == 'delete':
            client.ipfs_destroy(args.ipfs_dapp_slug)

    elif args.cmd == 'github':
        if args.github_cmd == 'list':
            client.github_list()
        elif args.github_cmd == 'read':
            client.github_retrieve(args.repo)
        elif args.github_cmd == 'fetch':
            if args.repo:
                client.github_fetch_repo(args.repo)
            else:
                client.github_fetch_all()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
