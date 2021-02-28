# Dhost-cli

Upload and host your website with DHost's CLI.

## Installation

```
git clone https://github.com/dhost-project/dhost-cli
```

On linux:
```
cd dhost-cli
chmod +x dhost.py
./dhost.py -h
```

## Commands

* `-h` : help message
* `-u USERNAME` : specify a username to connect with
* `-t TOKEN` : specify a token to connect with
* `-T` : get your token from your credentials
* `-a API_URL` : specify the API URL
* `app` : manage you apps
    * `create APP_NAME` : create a new app
    * `infos APP_NAME` : get details about an app
    * `list` : list apps
    * `delete APP_NAME` : delete an app

