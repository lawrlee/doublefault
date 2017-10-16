# Double Fault [![Build Status](https://travis-ci.org/lawrlee/doublefault.svg?branch=master)](https://travis-ci.org/lawrlee/doublefault) [![Coverage Status](https://coveralls.io/repos/github/lawrlee/doublefault/badge.svg?branch=master)](https://coveralls.io/github/lawrlee/doublefault?branch=master)

An open source Question/Answer platform inspired by Stack Overflow. On the server side it uses

- Python 2.7
- Django
- Graphene (GraphQL)
- PyTest

And on the client side

- React
- Blueprint.js
- Apollo
- Webpack

This aims to have near complete feature set with a Q/A platform akin to Stack Overflow or Quora. 
Users have the ability to ask questions, and other users can add answers to the questions. Users 
can also add comments to both questions and answers. The question OP can approve an answer. Users
can also up/down vote comments, answers, and questions. 

*The project is considered in early development mode and does not have full functionality.* 

# Installation

The easiest way to install is to use Docker and Docker Compose. You will have to make
some modifications prior to running to get full functionality.

1. Authentication

   The default configuration uses [social-app-django](https://github.com/python-social-auth/social-app-django) with Google Oauth2. These environment
   variables need to be set
   
   ```
   GOOGLE_OAUTH_KEY
   GOOGLE_OAUTH_SECRET
   ```
   
   Please change to an appropriate backend for your use.
   
2. Database

   The default database is a PostgreSQL database reachable at the `df-postgres` host at port 5432. Change
   the `DATABASES` section in `settings.py` to customize.

  
## Building/running Docker container

To run DoubleFault in a Docker container

```commandline
docker-compose up
```

This will execute `start.sh` which

1. Run migrations
1. Creates the client bundle using `webpack`.
1. Starts a gunicorn server in the container bound to `0.0.0.0:8080`.

The webserver should be accessible from your host at `localhost:8080`, assuming no
other services are using ports 8080 and 5432.

# Contributing

It is recommended to use Docker in your development process for environment parity. Enter
the container shell with something like

```commandline
docker-compose run --service-ports web bash
```

Then within the Docker container you can use webpack to watch your client code

```commandline
# ./node_modules/.bin/webpack --config webpack.config.js --watch &
```

load some initial testing fixtures

```commandline
# ./manage.py loaddata tests/test_fixtures.json
```

and run the Django webserver

```commandline
# ./manage.py runserver 0.0.0.0:8080
```

## Adding GraphQL queries/mutations/types

The schema used by Graphene is located in `web/schema/*`. There are separate files for 
types, queries, and mutations. The mutations should be complete and allow for creating/editing
of questions, answers, and comments. 

## Installing new dependencies

[pip-tools](https://github.com/jazzband/pip-tools) is used to manage dependencies. Any new 
dependencies should be added to `requirements.in` and compiled using

```commandline
pip-compile --output-file requirements.txt requirements.in
```

## Testing

[pytest](https://docs.pytest.org/en/latest/) is used for testing instead of the default Django test runner. Use the `test_settings.py` settings for running tests with Sqlite3 instead of posgres.

```commandline
pytest --ds=test_settings tests
```

running pdbpp

```commandline
pytest --pdb --ds=test_settings tests
```

Updating snapshots

```commandline
pytest --ds=test_settings --snapshot-update tests
```