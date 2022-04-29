#docker run -it alpine /bin/sh
# https://github.com/diyan/pgcli-docker
FROM python:alpine3.15
USER root
RUN apk add postgresql-dev build-base openssl && \
    apk add --update libpq && \
    pip install pgcli==2.1.1 --only-binary psycopg2
RUN chmod 777 /usr/local/bin/pgcli

USER guest
