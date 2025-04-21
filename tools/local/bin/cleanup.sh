#!/usr/bin/env bash

docker-compose -f ./tools/local/docker/docker-compose.yaml -f ./tools/local/docker/docker-compose.airflow.yaml down -v;
rm -rf ./tools/local/temp/;
rm -rf venv;