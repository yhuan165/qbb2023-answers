# Step 1.1

Rscript runChicago.R --design-dir ./raw/Design/ --en-feat-list ./raw/Features/featuresGM.txt --export-format washU_text ./raw/PCHIC_Data/GM_rep1.chinput,./raw/PCHIC_Data/GM_rep2.chinput,./raw/PCHIC_Data/GM_rep3.chinput ./output

# Step 1.2
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.

CTCF --> makes some sense because they would be enriched in the interactions of the domains interacting with eachother and CTCFs are making the boundaries
H3K4me1 --> I think it makes sense because this interacts directly with promoters, that H3K4me1 at promoters is not only linked to gene repression but also plays a role in limiting the recruitment of H3K4me3-interacting proteins. 
H3K4me3 --> enriched because genes are expressed in H3K4me3 regions that are euchromatin. 
H3K27ac --> makes sense to be enriched as it is associated with higher activation of transcription and an active enhancer mark which would be enriched in the promoter baited regions. 
H3K27me3 --> makes sense to be not enriched as it is for silencing regions (heterochromatin) and we baited for promoter interacting regions (which would most likely be not silence)
H3K9me3 --> does not make sense to be enriched because it should be associated with regions that should be constitutive heterochromatin that should be constantly repressed (eg. centromeres).  

#

