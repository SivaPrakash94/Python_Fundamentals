''' Goal:  Learn to parse column-aligned text intended for humans

    Output from:
        # show ipv4 interfaces brief
'''

from pprint import pprint
from typing import NamedTuple

class Interface(NamedTuple):
    name: str
    ipaddr: str
    status: str
    protocol: str

def parse_interfaces(source):
    'Parse "show ipv4 interfaces brief" into a list of Interface objects.'
    interfaces = []
    it = iter(source)
    heading = next(it)
    name_start = heading.index('Interface')
    ipaddr_start = heading.index('IP-Address')
    status_start = heading.index('Status')
    protocol_start = heading.index('Protocol')
    for interface in it:
        # name, ipaddr, status, protocol = interface.split()
        name = interface[name_start : ipaddr_start].rstrip()
        ipaddr = interface[ipaddr_start : status_start].rstrip()
        status = interface[status_start : protocol_start].rstrip()
        protocol = interface[protocol_start : ].rstrip()
        row = Interface(name, ipaddr, status, protocol)
        interfaces.append(row)
    return interfaces

if __name__ == '__main__':

    with open('data/ipv4_int_bri.txt') as f:
        for name, ipaddr, status, protocol in parse_interfaces(f):
            if status.casefold() == 'up':
                print(f'{ipaddr:15} {name}')

