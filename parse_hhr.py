import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--protein', required=True)

args = parser.parse_args()
args = dict(vars(args))
protein = args.get('protein')

hhpred_files = list(glob.glob('{}/hhpred_output/*.hhr'.format(protein)))
hhblits_files = list(glob.glob('{}/hhblits_output/*.hhr'.format(protein)))

with open('{}/hhpred_output.txt'.format(protein), 'w') as w:
    w.write('LABELS\n')
    w.write('SEPARATOR TAB\n')
    w.write('DATA\n')
    with open('{}/hhpred_output_tabular.tsv'.format(protein), 'w') as w2:
        for hhr_file in hhpred_files:
            seq_id = hhr_file.split('/')[-1].split('.')[0]
            with open(hhr_file, 'r') as f:
                i = 0
                j = 0
                w.write(seq_id + '\t')
                for line in f:
                    if line[0] == '>' and i == 0:
                        hit_info = line.split('>')[1].split(';')[0].split(' ', 1)[1]
                        if hit_info.startswith('Uncharacterized') or hit_info.startswith('uncharacterized') or hit_info.startswith('Hypothetical') or hit_info.startswith('hypothetical'):
                            skip = True
                            pass
                        else:
                            w.write(seq_id + ' ' + hit_info + '\n')
                            w2.write(seq_id + '\t' + hit_info + '\t')
                            i = 1
                            skip = False
                    elif line.startswith('Probab') and j == 0 and skip == False:
                        probab = line.split('  ')[0]
                        evalue = line.split('  ')[1]
                        score = line.split('  ')[2]
                        w2.write(probab + '\t' + evalue + '\t' + score + '\n')
                        j = 1
                    else:
                        pass

with open('{}/hhblits_output.txt'.format(protein), 'w') as w:
    w.write('LABELS\n')
    w.write('SEPARATOR TAB\n')
    w.write('DATA\n')
    with open('{}/hhblits_output_tabular.tsv'.format(protein), 'w') as w2:
        for hhr_file in hhblits_files:
            seq_id = hhr_file.split('/')[-1].split('.')[0]
            with open(hhr_file, 'r') as f:
                i = 0
                j = 0
                w.write(seq_id + '\t')
                for line in f:
                    if line[0] == '>' and i == 0:
                        hit_info = line.split('>')[1].split(';')[0].split(' ', 1)[1]
                        if hit_info.startswith('Uncharacterized') or hit_info.startswith('uncharacterized') or hit_info.startswith('Hypothetical') or hit_info.startswith('hypothetical'):
                            pass
                        else:
                            w.write(seq_id + ' ' + hit_info + '\n')
                            w2.write(seq_id + '\t' + hit_info + '\t')
                            i = 1
                    elif line.startswith('Probab') and j == 0 and i == 1:
                        probab = line.split('  ')[0]
                        evalue = line.split('  ')[1]
                        score = line.split('  ')[2]
                        w2.write(probab + '\t' + evalue + '\t' + score + '\n')
                        j = 1
                    else:
                        pass
