#!/bin/bash

set -eo pipefail

docker compose exec workspace ./generate_model.py
