#!/bin/bash

# step 1.1
bwa index sacCer3.fa

# step 1.2
for sample in *.fastq
do
	echo 'aligning samples:' ${sample}  
	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
		sacCer3.fa \
		${sample} > ${sample}.sam
done

# step 1.3
for samfile in *.sam
do
	echo 'sorting sam:' ${samfile}
	samtools sort ${samfile} -o ${samfile}.bam
done

for bamfile in *.bam
do
	samtools index ${bamfile} -b
done 

# step 2.1
ls *.bam > bam_list
freebayes -p 1 -f sacCer3.fa --genotype-qualities -L bam_list > allvar.vcf

# step 2.2 
vcffilter allvar.vcf -f "QUAL > 20" > filtervar.vcf

# step 2.3
vcfallelicprimitives filtervar.vcf -k -g > decomposedvar.vcf

# step 2.4
snpEff download R64-1-1.105
snpEff ann R64-1-1.105 decomposedvar.vcf > final.vcf 
