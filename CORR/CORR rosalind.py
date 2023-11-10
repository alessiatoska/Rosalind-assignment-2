#CORR rosalind

from Bio import SeqIO

seq_name, seq = [], []
    
for seq_record in SeqIO.parse('corr.txt','fasta'):
    seq_name.append(str(seq_record.name))
    seq.append(str(seq_record.seq))

def hamm(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

def proofread(reads):
    corrections = []
    incorr=[]
    corr = []
    reverse={"A": "T", "T": "A", "C": "G", "G": "C"}

    for i in reads:
        rev = "".join([reverse[j] for j in i[::-1]])
        if reads.count(i) + reads.count(rev) >= 2:
            corr.append(i)
        else:
            incorr.append(i)

    for wrong in incorr:
        for right in corr:
            revc = "".join([reverse[j] for j in right[::-1]])
            if hamm(wrong, right) == 1:
                corrections.append((wrong, right))
                break
            if hamm(wrong, revc) == 1:
                corrections.append((wrong, revc))
                break

    return corrections


corrections = proofread(seq)
for wrong, right in corrections:
    print("{}->{}".format(wrong, right))
    


#this other way doesn't work for the large dataset
'''
from collections import Counter
from Bio import SeqIO

def revc(dna):
    complement = str.maketrans('ATCG', 'TAGC')
    return dna.translate(complement)[::-1]

def hamming(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

sequences = (str(seq_record.seq) for seq_record in SeqIO.parse('corr.txt', 'fasta'))

count = Counter(sequences)
corr = {revc(seq) for seq in count if count[seq] >= 2 or revc(seq) in count}

corrections = {}

for wrong in count:
    for right in corr:
        if hamming(wrong, right) == 1:
            corrections[wrong] = right
            break

for wrong, right in corrections.items():
    print('{} -> {}'.format(wrong, right))
'''

