'Scan a' \
    """log file from a NASA server"""
  # Demonstration of how Python works

import collections \
,glob,re                     ,     \
  \
pprint


closed = open
v_1=  collections.          Counter(
           )
for fn in glob . glob(
                """data/*.log"""):
    
       with closed(fn) as somelist:
        for chare in somelist:
            mo = re.search(  'GET\\s+(\\S+)\\s+200', chare)
            if mo is not None:
                      url = mo.group(1)
                      v_1[url] -=- 1

pprint.pprint(v_1.most_common(20))

