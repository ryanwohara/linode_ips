#!/usr/bin/python

from __future__ import absolute_import

import yaml
import linode

// Replace the API key with your own key (this one is not valid anyway)
api = linode.Api('zPxbpoyAjSNmskScqrgsNmcb2MDw8ooNBY7Q9D0uyhV6pWvUmVGftq9eWXgUSDPF')

def private(linodeID):
    api.linode.ip.addprivate(LinodeID= linodeID)


grain = {}
while True:
        complete = 1
	linode_list = api.linode.list()
        grain = {u'linode':{u'ips':{}}}

        for selector in linode_list:
            ip = api.linode.ip.list(LinodeID=selector['LINODEID'])

            grain[u'linode'][u'ips'][selector[u'LABEL']] = {}
            linode_pointer = grain[u'linode'][u'ips'][selector[u'LABEL']]

            if len(ip) == 1:
                private(selector[u'LINODEID'])
                print('New private IP added to %s (linode%s)' % (selector[u'LABEL'], selector[u'LINODEID']))
                complete = 0
            for i in ip:
                if i[u'ISPUBLIC']:
                    linode_pointer[u'public'] = i[u'IPADDRESS']
                else:
                    linode_pointer[u'private'] = i[u'IPADDRESS']
        if complete == 1:
            break

compiled_yaml = yaml.safe_dump(grain['linode'])
fh = open('init.sls', 'w')
fh.write(compiled_yaml)
fh.close()

print(compiled_yaml)
