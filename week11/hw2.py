#!/usr/bin/env python

from matplotlib import pyplot as plt
import scanpy as sc

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

