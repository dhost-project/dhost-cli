#!/usr/bin/env python

"""
 ____  _   _           _         ____ _     ___
|  _ \| | | | ___  ___| |_      / ___| |   |_ _|
| | | | |_| |/ _ \/ __| __|____| |   | |    | |
| |_| |  _  | (_) \__ \ ||_____| |___| |___ | |
|____/|_| |_|\___/|___/\__|     \____|_____|___|

Command-line interface script for dhost.
"""
import argparse
import sys
import requests

from dhost_cli import settings
from dhost_cli.ipfs_dapp_api import IPFSDappManagement


def main():
    parser = argparse.ArgumentParser(
        prog='dhost',
        description='%(prog)s CLI tool to host decentralized websites.'
    )

    parser.add_argument(
        '-u', '--username', help="Connect to API with username and password."
    )
    parser.add_argument('-t', '--token', help="Connect to API with token.")
    parser.add_argument(
        '-T',
        '--get-token',
        action='store_true',
        help="Get your API token from username and password."
    )
    parser.add_argument('-a', '--api_url', default=settings.DEFAULT_API_URL)

    subparser = parser.add_subparsers(dest='cmd')

    ipfs_dapp = subparser.add_parser('ipfs', help="Manage you IPFS dapps.")
    ipfs_dapp_sub = ipfs_dapp.add_subparsers(dest='ipfs_dapp_cmd')
    # ipfs_dapp list
    list_ipfs_dapp = ipfs_dapp_sub.add_parser('list', help="List IPFS dapps.")
    # ipfs_dapp create
    create_ipfs_dapp = ipfs_dapp_sub.add_parser('create', help="Create a new IPFS dapp.")
    create_ipfs_dapp.add_argument('-n', '--name')
    # ipfs_dapp infos
    detail_ipfs_dapp = ipfs_dapp_sub.add_parser('infos', help="Get details about an IPFS dapps.")
    detail_ipfs_dapp.add_argument('ipfs_dapp_id')
    # ipfs_dapp update
    update_ipfs_dapp = ipfs_dapp_sub.add_parser('update', help="Update an IPFS dapp.")
    update_ipfs_dapp.add_argument('ipfs_dapp_id')
    # ipfs_dapp delete
    delete_ipfs_dapp = ipfs_dapp_sub.add_parser('delete', help="Delete an IPFS dapp.")
    delete_ipfs_dapp.add_argument('ipfs_dapp_id')

    args = parser.parse_args()

    if args.get_token:
        print('Token: ' + instance.get_token())

    if args.cmd == 'ipfs':
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
            instance.create(args.name)
        elif ipfs_dapp_cmd == 'delete':
            instance.delete(args.ipfs_dapp_id)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
