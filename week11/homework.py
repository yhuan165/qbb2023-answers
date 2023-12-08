#!/usr/bin/env python

from matplotlib import pyplot as plt
import scanpy as sc

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 


#1.1
sc.pp.neighbors(adata,n_neighbors=10, n_pcs=40)

#1.2
sc.tl.leiden(adata)

#1.3
sc.tl.umap(adata, maxiter = 900)
sc.tl.tsne(adata)
'''
fig, ax = plt.subplots(ncols=2)
sc.pl.umap(adata, color='leiden', show = False, title = "UMAP", ax = ax[0])
sc.pl.tsne(adata, color='leiden', show = False, title = "tSNE", ax = ax[1])

fig.tight_layout()
fig.savefig("exercise1.png")
#plt.show()
'''

#2.1
adata_copy = adata.copy()
wilcoxon_adata = sc.tl.rank_genes_groups(adata_copy,groupby='leiden', method = 'wilcoxon', use_raw=True, copy=True)
logreg_adata = sc.tl.rank_genes_groups(adata_copy, groupby='leiden',method = 'logreg', use_raw=True, copy=True)

# fig, ax = plt.subplots()
# sc.pl.rank_genes_groups(wilcoxon_adata, n_genes = 25, sharey=False, show=False, use_raw=True, title = "wilcoxon", save = "_wilcoxon.png")
# ax.set_title("Wilcoxon Rank-Sum")
# fig.tight_layout()
# fig.savefig("exercise2_wilcoxon.png")
# plt.show()



# sc.pl.rank_genes_groups(logreg_adata, n_genes = 25, sharey=False, show=False, use_raw=True, title = "logreg", save = "_logreg.png")

# fig.tight_layout()
# fig.savefig("exercise2_logreg.png")
# plt.show()

leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')

