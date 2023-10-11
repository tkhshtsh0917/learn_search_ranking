#!/bin/bash

set -eo pipefail

docker compose exec workspace \
    ./scatter_plot.py benchmark-mlr.txt scatter-mlr.png
