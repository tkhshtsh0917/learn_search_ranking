#!/bin/bash

set -eo pipefail

docker compose exec workspace head -2 baseline.txt.group
