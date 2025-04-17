#!/usr/bin/env bash

docker-compose -f ./tools/local/docker/docker-compose.yaml down -v;
rm -rf ./tools/local/temp/;
rm -rf venv;