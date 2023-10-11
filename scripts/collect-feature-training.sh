#!/bin/bash

set -eo pipefail

docker compose exec workspace \
    ./collect_responses.py feature hands_on_featuredata.txt.training hands_on_keywords.txt.training
