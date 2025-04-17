#!/usr/bin/env bash

docker-compose -f ./tools/local/docker/docker-compose.yaml up postgres kafka -d; \
docker-compose -f ./tools/local/docker/docker-compose.yaml \
               -f ./tools/local/docker/docker-compose.airflow.yaml up airflow-init;

python3 -m venv venv;
source venv/bin/activate; \
pip install -r requirements.txt;