#!/bin/bash

set -o allexport
source .env
set +o allexport

python -m fastapi dev app