#! /bin/bash

THIS_SCRIPT="$( realpath "$0" )"
THIS_PATH="$( dirname "$THIS_SCRIPT" )"

DEFAULT_BOOTSTRAP_NAME="$( basename "$( dirname "$THIS_PATH" )" )"
BOOTSTRAP_NAME="${BOOTSTRAP_NAME:=${DEFAULT_BOOTSTRAP_NAME}}"

BOOTSTRAP_BRANCH=${BOOTSTRAP_BRANCH:=master}
BOOTSTRAP_PY="https://raw.githubusercontent.com/lalmeras/clickable_bootstrap/${BOOTSTRAP_BRANCH}/bootstrap.py"

# environment.yml and pyproject.toml must me in cwd
cd "${THIS_PATH}"
wget -q -O - "${BOOTSTRAP_PY}" | BOOTSTRAP_COMMAND="poetry config settings.virtualenvs.create false && poetry install" python - --name "$BOOTSTRAP_NAME"
