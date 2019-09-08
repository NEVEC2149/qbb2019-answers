$head -n 40000 SRR072903.fastq > SRR072903.10k.fastq
$fastqc SRR072903.fastq
$hisat2 -p 4 -x ~/qbb2019-answers/genomes/BDGP6 -U SRR072903.fastq
$samtools sort -@ 4 SRR072903.10k.sam -o SRR072903.10k.bam
$samtools index SRR072903.10k.bam
$stringtie SRR072903.10k.bam -e -B -p 4 -G ~/qbb2019-answers/day1-morning/BDGP6.Ensembl.81.gtf -o SRR072903.gtf


Question 3
$grep "2L" SRR072893.sam | wc -l
$grep "2R" SRR072893.sam | wc -l
$grep "3L" SRR072893.sam | wc -l
$grep "3R" SRR072893.sam | wc -l
$grep "4" SRR072893.sam | wc -l
$grep "X" SRR072893.sam | wc -l
$grep "Y" SRR072893.sam | wc -l
number of lines indicate the number of alignments for each chromosome.


Question 4
"NF" in the awk command line means number of fields, it can be 12, 13, 20, 21, or 22 for the file SRR072893.sam
In each line of the .sam file, there are 11 mandatory lines and some tab-separated optional fields.

Lines with 12 fields contain 1 optional field, YT:Z:UU, indicating the read was not part of a pair
Lines with 13 fields contain an extra tag YF, indicating they are filtered out
Lines with 20 fields contain tags AS, XN, XM, XO, XG, NM, MD, YT and NH, suggesting they are aligned reads
Lines with 21 fields have an extra tag XS, indicating they are sliced alignments and can be mapped to one of the strand
Lines with 22 fields get an extra tag ZS, it marks the alighment of reads that involved SNPs