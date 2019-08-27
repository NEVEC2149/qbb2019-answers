$fastqc SRR072903.fastq
$hisat2 -p 4 -x ~/qbb2019-answers/genomes/BDGP6 -U SRR072903.fastq
$samtools sort -@ 4 SRR072903.10k.sam -o SRR072903.10k.bam
$stringtie SRR072903.10k.bam -e -B -p 4 -G ~/qbb2019-answers/day1-morning/BDGP6.Ensembl.81.gtf -o SRR072903.gtf
