import subprocess
import glob
proteomes = list(glob.glob('./databases/Chordata/proteomes/reduced_proteomes/MYOLUC.fasta'))

for proteome in proteomes:
   direction = proteome.split('.')[1].split('/')[-1]
#   print(direction)
#   print(proteome)
#   subprocess.run(['mkdir', './results/BUSCO/{}']).format(direction)
   print('now doing', '{}'.format(proteome))
   subprocess.run(['busco', '-i', '{}'.format(proteome), '-l','eukaryota_odb10', '-m', 'prot', '-o', 'results/BUSCO/Chordata/{}/'.format(direction), '--cpu', '10', '-e', '0.001', '-f'])
   print('finished','{}'.format(proteome))
