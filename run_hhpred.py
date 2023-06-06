import subprocess
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--protein', required=True)
parser.add_argument('-c', '--cpu', required=True)

args = parser.parse_args()
args = dict(vars(args))
protein = args.get('protein')
cpu = args.get('cpu')

seqs = list(glob.glob('{}/predicted_seqs_split/*fasta'.format(protein)))
#seqs = list(glob.glob('{}/seqs/hmmsearch_chordata/chordata/*fasta'.format(protein)))

subprocess.run(['mkdir', '{}/hhpred_output'.format(protein)])
subprocess.run(['mkdir', '{}/hhblits_output'.format(protein)])

for seq in seqs:
    seq_id = seq.split('/')[-1].split('.')[0]
    print(seq_id)
    subprocess.run(['hhblits', '-cpu', cpu, '-o', '{}/hhblits_output/'.format(protein) + seq_id + '.hhr', '-i', seq, '-oa3m', '{}/'.format(protein) + seq_id + '.a3m', '-e', '1e-3', '-n', '1', '-p', '20', '-Z', '250', '-z', '1', '-b', '1', '-B', '250', '-d', '/home/max/NOBINFBACKUP/uniref30_2022_02_hhsuite/UniRef30_2022_02'])
    subprocess.run(['hhsearch', '-cpu', cpu, '-o', '{}/hhpred_output/'.format(protein) + seq_id + '.hhr', '-i', '{}/'.format(protein) + seq_id + '.a3m', '-d', '/home/max/NOBINFBACKUP/pdb70_from_mmcif_2022_04_14/pdb70', '-p', '20', '-Z', '250', '-loc', '-z', '1', '-b', '1', '-B', '250', '-ssm', '2', '-sc', '1', '-seq', '1', '-dbstrlen', '10000', '-norealign', '-maxres', '32000'])
#    subprocess.run(['rm', '-f', '{}/'.format(protein) + seq_id + '.a3m'])
#    subprocess.run(['rm', '-f', '{}/'.format(protein) + seq_id + '.tmp'])
