import subprocess
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--protein', nargs = '+', required=True)

args = parser.parse_args()
args = dict(vars(args))
proteins = list(args.get('protein'))

for protein in proteins:
    hits = list(glob.glob('{}/hit_seqs_tblastn/*.fasta'.format(protein)))
    subprocess.run(['mkdir', '{}/augustus_gffs/'.format(protein)])
    subprocess.run(['mkdir', '{}/predicted_seqs/'.format(protein)])
    for hit in hits:
        hit_id = hit.split('/')[-1].split('.')[0]
        subprocess.run(['augustus', '--species=human', '--AUGUSTUS_CONFIG_PATH=/home/mick/Augustus/config/', '--outfile={}/augustus_gffs/{}.gff'.format(protein, hit_id), hit])
        subprocess.run(['getAnnoFasta.pl', '{}/augustus_gffs/{}.gff'.format(protein, hit_id)])
        subprocess.run(['mv', '{}/augustus_gffs/{}.aa'.format(protein, hit_id), '{}/predicted_seqs/{}.fasta'.format(protein, hit_id)])
