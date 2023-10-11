#!/bin/bash

set -eo pipefail

docker compose cp workspace:workspace/scatter-mlr.png .
