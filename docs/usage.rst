.. highlight:: shell

=====
Usage
=====

To use Dhost CLI in a project:

.. code-block:: console

    dhost-cli -h

You have a list of categories available:


IPFS
----

To control your IPFS dapps.

.. code-block:: console

    dhost-cli ipfs -h

.. code-block:: console

   usage: dhost ipfs [-h] {list,new,ret,update,delete,deploy} ...

   positional arguments:
     {list,new,ret,update,delete,deploy}
       list                List IPFS dapps.
       new                 Create a new IPFS dapp.
       ret                 Retrieve an IPFS dapps.
       update              Update an IPFS dapp.
       delete              Delete an IPFS dapp.
       deploy              Deploy an IPFS dapp.

   optional arguments:
     -h, --help            show this help message and exit

Dapps
-----

To view a list of your dapps and their status.

.. code-block:: console

    dhost-cli dapps -h

.. code-block:: console

   usage: dhost dapps [-h] {list,ret} ...

   positional arguments:
     {list,ret}
       list      List all dapps.
       ret       Retrieve a dapp.

   optional arguments:
     -h, --help  show this help message and exit


Github
------

If your account is connected to Github, it can be used to update your repos, branches to connect them to your dapp.

.. code-block:: console

    dhost-cli github -h

.. code-block:: console

   usage: dhost ipfs [-h] {list,new,ret,update,delete,deploy} ...

   positional arguments:
     {list,new,ret,update,delete,deploy}
       list                List IPFS dapps.
       new                 Create a new IPFS dapp.
       ret                 Retrieve an IPFS dapps.
       update              Update an IPFS dapp.
       delete              Delete an IPFS dapp.
       deploy              Deploy an IPFS dapp.

   optional arguments:
     -h, --help            show this help message and exit
