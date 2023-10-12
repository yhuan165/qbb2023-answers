Question 2:
Sample 1 peaks: 181 peaks
Sample 2 peaks: 193 peaks
Combined peaks: 172 peaks

95% peaks from sample 1 and 89% of peaks from sample 2

Question 3:
How reproducible are the peaks called between the two samples? Is the p-value range of a peak indicative of reproducibility? Is it completely consistent?

The peaks called between the two samples should be pretty reproducible as we have the peaks where the p-values are less than 1e-10, which demonstrates that these peaks are not random and most likely actual data peaks from Chip seq, and therefore reproducible. Many of these peaks also are the same as seen from question 2 there is a high number of overlap. However, it is not completely consistent as even seen in sample 1 and 2 peaks, only a portion of the peaks overlap in the combined peaks. Furthermore, there are certain wiggle peaks that are not seen in the bedfile, indicating that there is inconsistency between p-value and the high non-overlapping peaks. 
