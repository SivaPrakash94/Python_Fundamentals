''' Learn two techniques for writing complex regexes.

Problem:  A broken large regex is shockingly difficult to debug.

Solution:  Incremental development

1) Start with a simple, but matching regex.
   Slowly add constraints and retest.
   If if doesn't match, now you know the cause
   (it was the part you just added).

2) Start with a large over-specific regex that matches.
   Slowly make it more general and retest.
   If if doesn't match, now you know the cause
   (it was the part you just added).
'''

from typing import NamedTuple
from pprint import pprint
import re

class Interface(NamedTuple):
    slot: int
    name: str
    macaddr: str
    irq: int
  
interface_pattern = re.compile(r'(\d+): Ext: (\S+)\s+:\saddress is\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}),\s+irq (\d{1,2})')

def parse_interfaces(extract):
    'Parse the output of "show version" giving a list of Interface objects.'
    interfaces = []
    for slot, name, macaddr, irq in interface_pattern.findall(extract):
        interface = Interface(int(slot), name, macaddr, int(irq))
        interfaces.append(interface)
    return interfaces

if __name__ == '__main__':

    with open('data/parse_demo1.txt') as f:
        extract = f.read()
    interfaces = parse_interfaces(extract)      
    pprint(interfaces)    
