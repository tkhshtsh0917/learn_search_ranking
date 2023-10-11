#!/bin/bash

set -eo pipefail

docker compose exec workspace ./calc_ndcg.py mlr.txt
