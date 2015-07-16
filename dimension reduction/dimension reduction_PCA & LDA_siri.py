"""
=======================================================
Comparison of LDA and PCA 2D projection of Siri dataset
=======================================================

The Siri dataset represents 3 kind of Siri classes (Type 1, Type 2, Type 3)
with 4 attributes: attr_SL, attr_SQ, attr_PL, attr_PW

Principal Component Analysis (PCA) applied to this data identifies the
combination of attributes (principal components, or directions in the
feature space) that account for the most variance in the data. Here we
plot the different samples on the 2 first principal components.

Linear Discriminant Analysis (LDA) tries to identify attributes that
account for the most variance *between classes*. In particular,
LDA, in contrast to PCA, is a supervised method, using known class labels.
"""


print(__doc__)

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.lda import LDA

# read in csv dataset
siri = np.loadtxt('Siri_data_with_class.csv', delimiter=',',skiprows=1, dtype={'names':('Attr_SL','Attr_SQ','Attr_PL','Attr_PW','class'),'formats':('f2','f2','f2','f2','S6')})
X = np.array([list(i)[:4] for i in siri])
y = np.array([int(list(i)[4][5:]) for i in siri])
target_names = np.array(['Type 1','Type 2','Type 3'])

# choose the top 2 best attributes by PCA algo
pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

#lda is a supervised method, use target y
## choose the top 2 best attributes by LDA algo
lda = LDA(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

# Percentage of variance explained for each components
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

# draw scatterplot
plt.figure()
for c, i, target_name in zip("rgb", [1, 2, 3], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, label=target_name)
plt.legend()
plt.title('PCA of SIRI dataset')

plt.figure()
for c, i, target_name in zip("rgb", [1, 2, 3], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
plt.legend()
plt.title('LDA of SIRI dataset')

plt.show()
