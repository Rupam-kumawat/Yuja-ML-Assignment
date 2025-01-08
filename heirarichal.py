# hierarchical_clustering.py
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def hierarchical_clustering(data, max_clusters=50):
    best_n_clusters = None
    best_score = -1
    for n_clusters in range(2, max_clusters):
        clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward', affinity='euclidean')
        labels = clustering.fit_predict(data)

        if len(set(labels)) > 1 and len(set(labels)) < len(data):
            score = silhouette_score(data, labels)
            if score > best_score:
                best_n_clusters = n_clusters
                best_score = score
    
    return best_n_clusters, best_score

def visualize_hierarchical(data, labels, n_clusters):
    plt.figure(figsize=(10, 7))
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', alpha=0.7)
    plt.title(f'Hierarchical Clustering with {n_clusters} Clusters')
    plt.xlabel('Feature 1 (scaled)')
    plt.ylabel('Feature 2 (scaled)')
    plt.show()
