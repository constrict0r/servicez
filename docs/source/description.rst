Description
------------------------------------------------------------------------------

Ansible role to manage system services.

This role performs the following actions:

- Ensure the requirements are installed.

- Ensure the current user can obtain administrative (root) permissions.

- If the **services_disable** variable is defined, stop and disable the
  services listed on it.

- If the **configuration** variable is defined, stop and disable the
  *services_disable* listed on it.

- If the **services** variable is defined, enable and start the services listed
  on it.

- If the **configuration** variable is defined, enable and start the services
  listed on it.

