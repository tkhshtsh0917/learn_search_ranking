#!/bin/bash

set -eo pipefail

docker compose exec workspace curl -X DELETE "http://search-engine:9200/_ltr"
