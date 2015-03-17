# linode_ips

Requirements: Python, Linode module (pip install linode)

## linode_ips_to_yaml.py
Pull server IP information from the Linode API and dump it into init.sls for SaltStack. If a Linode does not have a private IP, it will be allocated (but private networking MUST be configured on the Linode to utilize it).

## regenerate_gluster_webservers.py
Store the private IP for all Linodes match "webserver*" in init.sls as YAML.
