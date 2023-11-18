#!/usr/bin/env bash
set -xe

isort --check .

black --check .

pytest

flake8 --ignore=E,W
