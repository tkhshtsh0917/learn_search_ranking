#!/bin/bash

set -eo pipefail

docker compose exec workspace wc -l hands_on_keywords.txt.test
