#!/bin/bash

set -eo pipefail

docker compose exec workspace head -2 hands_on_keywords.txt.test
