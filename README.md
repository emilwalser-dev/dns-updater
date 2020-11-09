# dns-updater

A DNS updater, that keeps the domain name up to date with the ip of the server.

Author: Emil Walser.

## TOC

- [TOC](#TOC)
- [About](#About)
- [Development](#Development)
  - [Prerequisites](#Prerequisites)
  - [Setup](#Setup)
  - [Environment](#Environment)
  - [Run](#Run)

## About

This utility changes the DNS records for the domain specified to the
application, whenever the public IP the utility sits behind changes, to always
reflect the correct IP address.

## Development

### Prerequisites

In order to set up a development environment you need to meet the
following requirements:

- `python`: ~3.8.0
- `pipenv`: ~2020.11.4

and optionally:

- `docker`: ~19.03.5 (to build the production-ready Docker image.)

### Setup

In order to set the project up you first need to install the required
dependencies.

Use the following command to install the required dependencies:

```
$ pipenv install
```

### Environment

In order to satisfy the environment for the application, you can
duplicate and rename the `example.env` file to `.env`.
Populate all variables before running the application.

If you are running the application in a docker container, you need to explicitly
define each environment variable required to run the application to docker
when starting the container. Below is an example command:

```
$ docker run --rm -it \
  --name dns-updater \
  -e GODADDY_KEY=key \
  -e GODADDY_SECRET=secret \
  -e GODADDY_DOMAIN=example.com \
  -e UPDATE_INTERVAL=5 \
  dns-updater
```

> NOTE: Make sure to build the docker image first.

### Run

In order to run the application you should have the pipenv virtual
environment activated.

Use the following command to activate the virtual environment:

```
$ pipenv shell
```

Now you can use the following command to start the application:

```
$ python src/main.py
```

Alternatively use the following command to run the app without activating
the virtual environment in your current shell.

```
$ pipenv run python src/main.py
```
