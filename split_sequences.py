from Bio import SeqIO
import subprocess
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--protein', required=True)

args = parser.parse_args()
args = dict(vars(args))
protein = args.get('protein')

hit_files = list(glob.glob('{}/predicted_seqs/*.fasta'.format(protein)))
subprocess.run(['mkdir', '{}/predicted_seqs_split'.format(protein)])
for hit_file in hit_files:
    hit_id = hit_file.split('/')[-1].split('.')[0]
    hits = SeqIO.parse(hit_file, 'fasta')

    for seq_record in hits:
        seq_record.id = hit_id + '_' + seq_record.id
        outfile = '{}/predicted_seqs_split/{}.fasta'.format(protein, seq_record)
        SeqIO.write(seq_record, outfile, 'fasta')
