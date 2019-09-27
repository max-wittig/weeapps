FROM python:3.8-alpine

ARG SECRET_KEY
ARG DJANGO_SETTINGS_MODULE
ARG USER=weeapps

WORKDIR /opt/weeapps

RUN apk add --no-cache \
      libffi-dev \
      openssl-dev \
      gcc \
      python3-dev \
      musl-dev && \
      addgroup -S "${USER}" && \
      adduser -S "${USER}" -G "${USER}" && \
      pip3 install --pre poetry

USER "${USER}"

COPY --chown="${USER}":"${USER}" . .

RUN poetry install --no-root -n && \
      poetry run python3 manage.py migrate

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "python3", "manage.py"]
CMD ["runserver", "--noreload", "0.0.0.0:8000"]
