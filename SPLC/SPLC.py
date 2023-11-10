#SPLC rosalind

from Bio import SeqIO
from Bio.Seq import Seq

with open("rnasplicing.txt", "r") as splc:
    sequence = list(SeqIO.parse(splc, "fasta"))

l = []
protein = str(sequence[0].seq)

for i in sequence[1:]:
    l.append(str(i.seq))

for j in range(len(l)):
    protein = protein.replace(l[j], '')

final_protein = Seq(protein)
final_protein=final_protein.translate(to_stop=True)

print(final_protein)
