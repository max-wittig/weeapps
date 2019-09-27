# weeapps

Little django application to play around with websockets and django channels

## installation

```sh
poetry install
poetry run python3 manage.py migrate
```

## usage

### to run locally

```sh
docker run -d --rm -p 6379:6379 redis
```

Make sure that you got redis and `REDIS_IP` environment variable set.
Defaults to localhost.

```sh
export SECRET_KEY=<some-secret-key>
export DJANGO_SETTINGS_MODULE=weeapps.settings.local
poetry run python3 manage.py runserver
```

### prod run

This allows you to use a reverse proxy like nginx.

```sh
export SECRET_KEY=<some-secret-key>
export DJANGO_SETTINGS_MODULE=weeapps.settings.prod
poetry run python3 manage.py runserver
```
