#%%
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
#%%
centers = np.array([[1, 1], [-1, -1], [1, -1]])
#%%
from matplotlib import pyplot as plt
X, labels_true = make_blobs(n_samples=750, centers=centers,
                            cluster_std=0.4, random_state=0)
X = StandardScaler().fit_transform(X)
#%%
db = DBSCAN(eps=0.3, min_samples=10)
db.fit(X)
#%%
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
#%%
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)
#%%
print(f'Количество кластеров : {n_clusters:}')
print(f'Количество аномальный значений : {n_noise}')
#%%
uniq = set(labels)
colors = ['red', 'blue', 'green', 'black']
for k, col in zip(uniq, colors):
    class_member_mask = (labels == k)
    xy = X[class_member_mask & core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1], marker='o', c=colors[k])
    xy = X[class_member_mask & ~core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1], marker='o', c=colors[k])
plt.show()

#