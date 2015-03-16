# linode_ips

Pull IP information from the Linode API and dump it into init.sls for SaltStack. If a Linode does not have a private IP, it will be allocated (but private networking MUST be configured on the Linode to utilize it).

Requirements: Python 2, Linode module
