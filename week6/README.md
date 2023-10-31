Exercise 1.1
plink --vcf genotypes.vcf --pca 10 --out PCA10

Exercise 2.1
plink --vcf genotypes.vcf --freq --out afs

Exercise 3.1
plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar PCA10.eigenvec --allow-no-sex --out phenotype_gwas_resultsCB

plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar PCA10.eigenvec --allow-no-sex --out phenotype_gwas_resultsGS

Exercise 3.4
rs10876043 (CB) --> DIP2B gene, involved in DNA methylation
rs7257475 (GS) --> ZNF826 gene, which is a Zinc finger protein which is involved in a lot of functions
In both cases, because these are fundamental proteins to normal function, a SNP in these proteins that might cause changes to the protein will definetly have an effect therefore a phenotypic trait. 