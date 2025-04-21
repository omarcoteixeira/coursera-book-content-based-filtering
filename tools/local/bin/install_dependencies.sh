#!/usr/bin/env bash

export REQUIREMENTS_FILE_PATH=$(pwd)'/requirements.txt' # Needed to force airflow to create at root folder

yes | cp -rf .env tools/local/docker/; # Docker compose limitation forces copy files to the same directory.
yes | cp -rf requirements.txt tools/local/docker/; # Docker compose limitation forces copy files to the same directory.

docker-compose -f ./tools/local/docker/docker-compose.yaml up postgres kafka -d; \
docker-compose -f ./tools/local/docker/docker-compose.yaml \
               -f ./tools/local/docker/docker-compose.airflow.yaml up airflow-init;

python3 -m venv venv;
source venv/bin/activate; \
pip install -r requirements.txt;