import re, sys, os, os.path
#import matplotlib.pyplot as plt

#### USAGE:  python read_clusters_mmseqs_declusterize.py DIRECTORY/ORIGINALSEQS.fasta DIRECTORY/CLUSTER-MMSEQS.tsv NAME  # name is the name of the file to be saved, and the working directory
## This script is to declusterize mmseqs clusters, trying to recover non-redundant sequences that were initially bad annotated as redundant
## It uses MSAs of mmseqs clsuters to infer seq-identity with its representative of the cluster, and with its closest seqs in the clusters. IMPORTANT: seq-dentity do not consider gaps. 

## USE PRINTS to controll the specfic cases to take a look closer...

from sys import argv
script, SEQS, CLUS, ORG = argv

os.system('mkdir -p new_nr_mmseqs')
os.system('mkdir -p %s' % ORG)

nspl = SEQS.split('/')
name = nspl[-1].replace('.fasta', '').replace('.fa', '')

seqfile = open(SEQS, 'r')
seqs = {}
for x in seqfile:
	x = x.strip()
	if x.startswith('>'):	
		h = x.replace('>', '')
		h = re.sub('\s.+', '', h)
		h = h.replace('|', '_')
		seqs[h] = []
	if not x.startswith('>'):
		seqs[h].append(x)
seqfile.close()


clusterfile = open(CLUS, 'r')
clusters = {}
for x in clusterfile:
	x = x.strip()
	spl = x.split('\t')
	rep = spl[0].replace('|', '_') # representative seq
	red = spl[1].replace('|', '_') # redundant seq
	if rep not in clusters:
		clusters[rep] = []
	clusters[rep].append(red)

clusterfile.close()

IDS = [] ## identities to plot. Identity with representative
IDS_reclassified = []	## identities to plot. Identity with closest 
nonredundant = []
newnr = {}
for x in clusters:
#	print x, len(clusters[x])
	if len(clusters[x]) > 1:
		nf = open(ORG+'/'+x+'.fa', 'w')

		## Write seqs ordered by length		
		slength = {}
		for s in clusters[x]:
			slength[s] = len(''.join(seqs[s]))
		orderedseqs = sorted(slength.items(), key=lambda item: item[1], reverse = True)
		for s,ll in orderedseqs:
			nf.write('>'+s+'\n'+''.join(seqs[s])+'\n')
		nf.close()

		mafft = 'mafft --anysymbol %s/%s.fa > %s/%s.afa' % (ORG, x, ORG, x)
		trimal = 'trimal -in %s/%s.afa -out %s/%s.gp.afa -gappyout' % (ORG, x, ORG, x)
		trident = 'trimal -in %s/%s.gp.afa -sident > %s/%s.matrix.txt' % (ORG, x, ORG,  x)
		
		if os.path.exists('%s/%s.gp.afa'% (ORG, x)) == False: 

			print (mafft)
			os.system(mafft)
			print (trimal)
			os.system(trimal)
			print (trident)
			os.system(trident)
		
		afa = open('%s/%s.gp.afa' % (ORG, x), 'r')  ## Read MSAs
		aseqs = {}
		for y in afa:
		        y = y.strip()
			if y.startswith('>'):
				h = y.replace('>', '')
				h = re.sub('\s.+', '', h)
				aseqs[h] = []
			if not y.startswith('>'):
				aseqs[h].append(y)

		
		identities = open('%s/%s.matrix.txt' % (ORG, x), 'r')
		v = 0
		nr = []
		for l in identities:
			l = l.strip()
			if len(l) == 0 :
				v = 0
			if v == 1:
				spl = l.split('\t')
				q, iden, target = spl[0].strip(), float(spl[1]), spl[-1].strip() #identity with closest
				ii, i, r, rr = 0, 0, 0, 0
				for n,m,o in zip(''.join(aseqs[q]), ''.join(aseqs[x]), ''.join(aseqs[target])): #Read MSA, to extract identities with representaitve and closest sequence excluding gaps
					#print n, m, o
					if n != '-' and m != '-':
						i = i+1
						if n == m:
							ii = ii+1
					if n != '-' and o != '-':
						r = r+1
						if n == o:
							rr = rr+1

#				print q,  ''.join(aseqs[q]) ## Print query, representative and closest aln seqs 
#				print x, ''.join(aseqs[x])
#				print target,  ''.join(aseqs[target])			

				if i == 0: ## This hanppens in very small partial seqs
					idenn = 0
				if i != 0:
					idenn = round(float(ii)/float(i), 2) #identity with representative without gaps

				if r == 0:
					idenn_closest = 0
				if r != 0:
					idenn_closest = round(float(rr)/float(r), 2) #identity with closest without gaps
	
##				print x, q, iden, idenn, idenn_closest  ## USE THIS PRINT TO SEE INDIVIDUAL SIMILARITIES
				newnr[q] = target
				IDS.append(idenn)
				if idenn < 0.99:				## identity threshold of query with representative ('x')
					IDS_reclassified.append(idenn_closest)
					if q != x and q not in nonredundant and target not in nonredundant:	##Make sure query is not an old reprsentative
						if q not in nr and target not in nr and len(''.join(seqs[q])) > 50:	## Make sure that query is not redundant with sequence already included
							nonredundant.append(q)
							nr.append(q)
							nr.append(target)
						if idenn_closest < 0.99 and q not in nonredundant and len(''.join(seqs[q])) > 50:
							nonredundant.append(q)
													
			if l.startswith('## Identity for most similar pair-wise sequences matrix') or l.startswith('#Percentage of identity with most similar sequence:'):
				v = 1



print('Sequences recovered in %s:' % name, len(nonredundant), 'representing', len(IDS_reclassified), 'sequences')

## Save new nr sequences

newfasta = open('new_nr_mmseqs/%s.rep.fasta' % name, 'w')
for x in nonredundant:
	newfasta.write('>'+x+'\n'+''.join(seqs[x])+'\n')		
for x in clusters:
	newfasta.write('>'+x+'\n'+''.join(seqs[x])+'\n')
newfasta.close()	 

os.system('rm -f -r %s/' % ORG)
sys.exit()


## Plot identity distribution 

fig, (ax1, ax2) = plt.subplots(2, figsize=(16, 10))
ax1.hist(IDS, density=False)
ax1.title.set_text('Identity with representative (IR) of mmseqs-cluster excluding gaps (%s)' % name)
for rect in ax1.patches:
	height = rect.get_height()
	ax1.annotate({int(height)}, \
xy = (rect.get_x() + rect.get_width() / 2, height), \
xytext = (0, 5), textcoords = 'offset points', ha = 'center', va = 'bottom')


ax2.hist(IDS_reclassified, density=False)
ax2.title.set_text('Identity of IR-sequences lower than 0.9, with closest seq in the mmseqs-cluster excluding gap. Sequences recovered: %s' % len(nonredundant))
for rect in ax2.patches:
	height = rect.get_height()
	ax2.annotate({int(height)}, \
xy = (rect.get_x() + rect.get_width() / 2, height), \
xytext = (0, 5), textcoords = 'offset points', ha = 'center', va = 'bottom')



fig.savefig('%s.png' % name)
