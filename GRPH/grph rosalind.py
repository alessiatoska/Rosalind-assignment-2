#GRPH rosalind

from Bio import SeqIO

records = list(SeqIO.parse("grph.txt", "fasta"))

overlap = 3
adjacency = {}

for i in range(len(records)):
    for j in range(len(records)):
        if i != j:
            seq1 = str(records[i].seq)
            seq2 = str(records[j].seq)
            if seq1[-overlap:] == seq2[:overlap]:
                if records[i].id not in adjacency:
                    adjacency[records[i].id] = []
                adjacency[records[i].id].append(records[j].id)

for key, values in adjacency.items():
    for value in values:
        print(f"{key} {value}")
