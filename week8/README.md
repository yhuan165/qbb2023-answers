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

# 2.2 
# The 6 top-scoring interactions between two promoters (2 bait)
chr20   44438565        44565593        .       1000    34.77   .       0       chr20   44562442        44565593        PCIF1   +       chr20   44438565        44442365        UBE2C   +

chr20  44438565  44607204  .  986   34.29  .  0  chr20  44596299  44607204  FTLP1;ZNF335                                     +  chr20  44438565  44442365  UBE2C  +

chr21   26837918        26939577        .       978     34.02   .       0       chr21   26837918        26842640        snoU13  +       chr21   26926437        26939577        MIR155HG        +

chr20  44452862  44565593  .  974   33.89  .  0  chr20  44562442  44565593  PCIF1                                            +  chr20  44452862  44471524  SNX21;TNNC2                                      +

chr20  17660712  17951709  .  973   33.85  .  0  chr20  17946510  17951709  MGME1;SNX5                                       +  chr20  17660712  17672229  RRBP1                                            +

chr20  24972345  25043735  .  973   33.84  .  0  chr20  24972345  24985047  APMAP                                            +  chr20  25036380  25043735  ACSS1                                            +

# The 6 top-scoring interactions between a promoter and an enhancer
chr21   26797667        26939577        .       952     33.13   .       0       chr21   26926437        26939577        MIR155HG        +       chr21   26797667        26799364        .       -

chr20   55957140        56074932        .       928     32.29   .       0       chr20   55957140        55973022        RBM38;RP4-800J21.3      +       chr20   56067414        56074932        .       -

chr21   26790966        26939577        .       838     29.17   .       0       chr21   26926437        26939577        MIR155HG        +       chr21   26790966        26793953        .       -

chr20  5585992   5628028   .  830   28.88  .  0  chr20  5585992   5601172   GPCPD1                                           +  chr20  5625693   5628028   .                                                -

chr21   26793954        26939577        .       754     26.23   .       0       chr21   26926437        26939577        MIR155HG        +       chr21   26793954        26795680        .       -

chr20  5515866   5933156   .  750   26.08  .  0  chr20  5929472   5933156   MCM8;TRMT6                                       +  chr20  5515866   5523933   .                                                -

# 2.3 - Does it make sense for this gene to be interacting with enhancers in GM12878? Explain.
For the second highest score, the gene located in this region is RBM38, its function include that: it is a RNA-binding protein that specifically bind the 3'-UTR of CDKN1A transcripts, leading to maintain the stability of CDKN1A transcripts, thereby acting as a mediator of the p53/TP53 family to regulate CDKN1A. (CDKN1A is a cyclin-dependent kinase inhibitor transcriptionally regulated by the p53/TP53 family to induce cell cycle arrest.) This makes sense to be interacting with enhancers in GM12878 as this is an essential gene for the functionality of the cell. 

For the 4th highest score, the gene located in this region is GPCPD1, it may be involved in the negative regulation of skeletal muscle differentiation. This makes less sense for this gene to be interacting with enhancers as the functions seems to be unclear. 


