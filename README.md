This project is a template for igloo application deployment

# Initialize a new project

* checkout a raw igloo-ansible project. Rename project folder as it is named to initialize virtualenv
  (bootstrap.sh script).
* delete ``.gitmodules`` and ``dependencies/igloo-ansible-playbooks`` and add it as a submodule
  * ``git submodule add git@github.com:igloo-project/igloo-ansible-playbooks``
  * ``git submodule update --init --remote``
* rename boostrap/igloo\_ansible to bootstrap/myproject.
* in bootstrap/pyproject.toml, rename igloo-ansible (2 occurrences)
  to myproject.
* run ``./bootstrap/bootstrap.sh``:
  * this script installs a miniconda environment with ``myproject`` command.
  * ``myproject`` command is handled by clickables.py file.
  * run the provided command at the end for the script for environment activation: ``source ...``.

* update ``inventory/hosts`` for vagrant hostnames and your deployment hostnames
* add debian hosts in debian group

* copy 01-igloo-minimal.yml and rename it to minimal.yml and update configuration.
* 01-igloo-extra.yml and 01-igloo-private.yml *can* be used to customize more items.
* rename folders/files in group\_vars and host\_vars and override values when needed
  * update ssl certificates' related values
  * update ``ansible_user`` used for ssh connection

# Migration for old project

* renamed: playbook\_environment -> playbook\_maven\_environment and playbook\_profile
* try to minimize overrided configurations

