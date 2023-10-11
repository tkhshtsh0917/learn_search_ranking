#!/bin/bash

set -eo pipefail

docker compose exec workspace bash -c 'ls hands_on_featuredata.*'
