# This counts the number of sequences in the sys arg passed FASTA file.

# it prints the number of sequence ids found.
# it prints the number of UNIQUE seq. ids found.

from Bio import SeqIO
import sys


print sys.argv

fn = sys.argv[1]

handle = open(fn, "rU")

seq_ids = []

for record in SeqIO.parse(handle, "fasta") :
    seq_ids.append(record.id)

print "Number of sequences found: %s" %(len(seq_ids))
print "Number of UNIQUE sequence IDS founds: %s" %(len(set(seq_ids)))

handle.close()


