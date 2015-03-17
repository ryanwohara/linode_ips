#!/usr/bin/python

from __future__ import absolute_import

import yaml
import linode

// Replace with your own API key (this one isn't valid anyway)
api = linode.Api('zPxbpoyAjSNmskScqrgsNmcb2MDw8ooNBY7Q9D0uyhV6pWvUmVGftq9eWXgUSDPF')

grain = {}
linode_list = api.linode.list()
grain = {u'linode':{u'webservers':{}}}

for selector in linode_list:
    ip_list = api.linode.ip.list(LinodeID=selector['LINODEID'])

    for ip in ip_list:
        if not ip[u'ISPUBLIC'] and selector[u'LABEL'].startswith('webserver'):
            grain[u'linode'][u'webservers'][selector[u'LABEL']] = {}
            linode_pointer = grain[u'linode'][u'webservers'][selector[u'LABEL']]
            linode_pointer[u'IP'] = ip[u'IPADDRESS']

compiled_yaml = yaml.safe_dump(grain['linode'])
fh = open('init.sls', 'w')
fh.write(compiled_yaml)
fh.close()

print(compiled_yaml)
