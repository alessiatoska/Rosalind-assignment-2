#LONG rosalind

from Bio import SeqIO

superstring=[]

for record in SeqIO.parse('long.txt', "fasta"):
        superstring.append(str(record.seq))
        length=len(str(record.seq))


for i in range(len(superstring)):
    for s1 in superstring:
        for s2 in superstring:
            if s1 != s2:
                for j in range(len(s1)):
                    if s1[:j] == s2[-j:] and j >= int(length//2)-1:
                        superstring.append(s2+s1[j:])
                        if s1 in superstring:
                            superstring.remove(s1)
                        if s2 in superstring:
                            superstring.remove(s2)
print(superstring)
