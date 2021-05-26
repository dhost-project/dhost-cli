=========
Dhost CLI
=========


.. image:: https://img.shields.io/pypi/v/dhost-cli.svg
        :target: https://pypi.python.org/pypi/dhost-cli

.. image:: https://img.shields.io/travis/2O4/dhost-cli.svg
        :target: https://travis-ci.com/2O4/dhost-cli

.. image:: https://readthedocs.org/projects/dhost-cli/badge/?version=latest
        :target: https://dhost-cli.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/2O4/dhost-cli/shield.svg
     :target: https://pyup.io/repos/github/2O4/dhost-cli/
     :alt: Updates


CLI to access the DHost services.

.. code-block::

   pip install dhost-cli

.. code-block::

    dhost-cli -h
    usage: dhost [-h] [-u USERNAME] [-t TOKEN] [-T] [-a API_URL] {ipfs} ...

    dhost CLI tool to host decentralized websites.

    positional arguments:
      {ipfs}
        ipfs                Manage you IPFS dapps.

    optional arguments:
      -h, --help            show this help message and exit
      -u USERNAME, --username USERNAME
                            Connect to API with username and password.
      -t TOKEN, --token TOKEN
                            Connect to API with token.
      -T, --get-token       Get your API token from username and password.
      -a API_URL, --api-url API_URL

* Free software: MIT license
* Documentation: https://dhost-cli.readthedocs.io.
