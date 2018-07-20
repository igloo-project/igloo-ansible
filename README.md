This project is a template for igloo application deployment

# Modification needed

* configure your own ssh keys (authorized\_keys.yml)
* configure letsencrypt support (common.yml)
* check database name (configured from application name by default) (common.yml)
* check notification filtering configuration (common.yml)
* configure your own groups if needed
* add your username in *local* group (inventory/hosts)
* modify playbook\_project\_git\_url (common.yml)
* check your smtp configuration


# TODO

Get rid of the need to add username in *local* group.
