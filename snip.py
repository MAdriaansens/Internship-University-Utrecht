import argparse
import glob
from Bio import SeqIO
import os

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--start', required=True)
parser.add_argument('-f', '--finish', required=True)

args = parser.parse_args()
args = dict(vars(args))
protein = '/home/mick/TBB_internship/HJURP/seqs/PFAM/SMC3/SACCER002416.fasta'
hit_start = args.get('start')
hit_end = args.get('finish')

protein_of_interest = SeqIO.parse('{}'.format(protein), 'fasta')
for seq_record in protein_of_interest:
                print(seq_record)
                hit_seq = seq_record.seq[1:212]
                with open('/home/mick/TBB_internship/CAL1/snipped/SACCER_N-terminus{}.fasta'.format(hit_end), 'w') as f:
                    f.write('>SACCER\n')
                    f.write(str(hit_seq) + '\n')

