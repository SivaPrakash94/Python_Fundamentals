'Scan a log file from a NASA server'

# Demonstration of how Python works

import collections
import glob
import re
import pprint

def frequent_urls(path):
    visited = collections.Counter()
    for filename in glob.glob(path):
        with open(filename) as f:
            for line in f:
                mo = re.search(r'GET\s+(\S+)\s+200', line)
                if mo is not None:
                    url = mo.group(1)
                    visited[url] += 1
    return visited

if __name__ == '__main__':

    visited = frequent_urls('data/*.log')
    pprint.pprint(visited.most_common(20))


