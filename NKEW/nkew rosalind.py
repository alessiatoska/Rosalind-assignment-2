#NKEW rosalind


from Bio import Phylo
from io import StringIO

dist = []
    
data = [seq.split('\n') for seq in open('nkew.txt').read().strip().split('\n\n')]
    
for i, j in data:
    x, y = j.split()
    tree = Phylo.read(StringIO(i), 'newick')
    dist.append(int(tree.distance(x, y)))
        
print(" ".join(str(x) for x in dist))
