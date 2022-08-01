[![Build Status](https://travis-ci.org/kevgathuku/compshop.svg)](https://travis-ci.org/kevgathuku/compshop)
[![Coverage Status](https://coveralls.io/repos/kevgathuku/compshop/badge.svg)](https://coveralls.io/r/kevgathuku/compshop)

## CompShop

A product display and advertising website for an online retail computer shop

Technologies used:
* [Python 3](https://python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](http://www.postgresql.org/)


### Dev Env Setup

For quick dev setup of the app, it's recommended to use `direnv`

- Install direnv.
- Create a `.envrc` file in the root directory with the following contents:
```
layout python3
export DJANGO_DEVELOPMENT=true
```

- Run `direnv allow`

Install the dependencies (Including dev dependencies):

```shell
pipenv install --dev
```
