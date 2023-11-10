#NWCK rosalind

from Bio import Phylo
from io import StringIO

with open('nwck.txt') as file:
    data = file.read().strip().split('\n\n')

dist = []

for i in data:
    i = i.strip()
    start, end = i.split('\n')[1].split()
    trees = Phylo.parse(StringIO(i), "newick")

    for j in trees:
        if j.find_any(start) and j.find_any(end):
            path = j.trace(start, end)
            if path and path[0].name == start:
                del path[0]
            dist.append(str(len(path)))

print(' '.join(dist))
