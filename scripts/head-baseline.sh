#!/bin/bash

set -eo pipefail

docker compose exec workspace head -20 baseline.txt
