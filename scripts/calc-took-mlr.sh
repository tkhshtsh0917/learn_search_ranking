#!/bin/bash

set -eo pipefail

docker compose exec workspace ./calc_took.py benchmark-mlr.txt
