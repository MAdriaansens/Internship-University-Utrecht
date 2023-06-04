#appending new proteome to large general proteome file

from Bio import SeqIO
imporsplt glob
genomes = list(glob.glob("./abbreviation/*.fasta"))
#genomes = ["/home/max/NOBINFBACKUP/Monocentrics/Proteomes/NotAnnotated/ACACAS.fasta"]
for genome in genomes:
      species_id = genome.split("/")[-1].split(".")[0]
      parsed_genome = SeqIO.parse(genome, "fasta")
      annotated_genome = list()
      for i, seq_record in enumerate(parsed_genome):
        i = format(i, '06d')
        seq_record.id = species_id + str(i)
        seq_record.description = ""
`       annotated_genome.append(seq_record)
