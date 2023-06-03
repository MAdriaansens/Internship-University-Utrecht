import multiprocessing as mp
from Bio import SeqIO
import glob
import os

genomes = list(glob.glob("to_be_done/*.fasta"))
def labeling(genome):i
    print("Now doing genome: {}".format(genome))
    species_id = genome.split("/")[-1].split(".")[0]
    parsed_genome = SeqIO.parse(genome, "fasta")
    annotated_genome = list()
    # print(species_id)
    for i, seq_record in enumerate(parsed_genome):
        i = format(i, '06d')
        seq_record.id = 'DNA_' + species_id + str(i)
        seq_record.description = ""
        annotated_genome.append(seq_record)
        #print(seq_record.id)
        outfile = "/home/mick/TBB_internship/databases/Eukarya5/genomes/single_genomes/done/results_relabeling/{}.fa".format(species_id)
        SeqIO.write(annotated_genome, outfile, "fasta")


with mp.Pool(processes=5) as pool:
    pool.map(labeling, genomes)
