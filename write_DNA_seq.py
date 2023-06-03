import sys
import os
from Bio import SeqIO
import argparse

protein = sys.argv[1]

new_hits_species = [x[0:6] for x in new_hits]

#hits against TBLASTN genome with protein of interest
for new_hit_species in new_hits_species:
    parsed_genome = SeqIO.parse('/home/mick/TBB_internship/databases/Eukarya5/genomes/abbreviation/done/correct/{}.fa'.format(new_hit_species),'fasta')
    for seq_record in parsed_genome:
        if  seq_record.id.split('_')[1] in new_hits:
            print(seq_record.id)
            
           
            with open('./{}vEUK5_fmt6_TBLASTN.tsv'.format(protein), 'r') as f:
                for line in f:
                    line = line.split('\t')
                    if line[1] == seq_record.id:
                        end = int(line[9]) +25000
                        start = int(line[8])-25000
                        if start < 0:
                           start = 0
            seq_interest = seq_record.seq[start:end]
            outfile = '/home/mick/TBB_internship/databases/Eukarya5/genomes/new_hits_tblastn_{}/{}.fa'.format(protein, new_hit_species)
            SeqIO.write(seq_interest,outfile,'fasta')
