import pandas as pd
import subprocess
import argparse
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--protein', nargs = '+', required=True)
parser.add_argument('-c', '--cpu', required=True)

args = parser.parse_args()
args = dict(vars(args))
proteins = list(args.get('protein'))
cpu = args.get('cpu')

genomes = list(glob.glob('/home/mick/TBB_internship/databases/Insecta/genomes/genome_databases/*'))
genomes_species = [x.split('/')[-1].split('.')[0] for x in genomes]
for protein in proteins:
    subprocess.run(['mkdir', '{}/tblastn_output'.format(protein)])
    ortho_ids = pd.read_csv('/home/mick/TBB_internship/{}/ids/HJURP_fl_ids.csv'.format(protein), sep = ',', header = None)
    ortho_ids = ortho_ids[0].tolist()
    ortho_ids_species = [x[0:6] for x in ortho_ids]
  #  print(ortho_ids) 
    ortho_seqs = list(glob.glob('/home/mick/TBB_internship/{}/seqs/PFAM/SMC3/*fasta'.format(protein)))
  #  print(ortho_seqs)
    genomes_no_ortho = [x for x in genomes_species if x not in ortho_ids_species]
    for genome_species in genomes_no_ortho:
#        print(genome_species)
        for ortho_seq in ortho_seqs:
            ortho_seq_species = ortho_seq.split('/')[-1].split('.')[0]
 #           print(ortho_seq_species)
            subprocess.run(['tblastn', '-query', ortho_seq, '-num_threads', cpu, '-db', '/home/mick/TBB_internship/databases/Insecta/genomes/genome_databases/{}.fasta'.format(genome_species), '-out', '{}/tblastn_output/{}_hitby_{}.tbl'.format(protein, genome_species, ortho_seq_species), '-outfmt', '6', '-evalue', '1e-5'])
            if os.stat('{}/tblastn_output/{}_hitby_{}.tbl'.format(protein, genome_species, ortho_seq_species)).st_size == 0:
                subprocess.run(['rm', '-f', '{}/tblastn_output/{}_hitby_{}.tbl'.format(protein, genome_species, ortho_seq_species)])
                print('removed {}/tblastn_output/{}_hitby_{}.tbl'.format(protein, genome_species, ortho_seq_species)) 
            else: 
                print('kept {}/tblastn_output/{}_hitby_{}.tbl'.format(protein, genome_species, ortho_seq_species))
