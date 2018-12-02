#! /bin/bash

BOOTSTRAP_PY="https://raw.githubusercontent.com/lalmeras/clickable/ft-ansible/bootstrap/clickable_bootstrap/bootstrap.py"
wget -q -O - "${BOOTSTRAP_PY}" | BOOTSTRAP_COMMAND="poetry install" python
