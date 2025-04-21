#!/usr/bin/env bash

export AIRFLOW_PROJ_DIR=$(pwd) # Needed to force airflow to create at root folder

echo "Copying files...";

yes | cp -rf .env tools/local/docker/; # Docker compose limitation forces copy files to the same directory.
yes | cp -rf requirements.txt tools/local/docker/; # Docker compose limitation forces copy files to the same directory.

echo "Starting docker...";
docker-compose -f ./tools/local/docker/docker-compose.yaml \
               -f ./tools/local/docker/docker-compose.airflow.yaml up;