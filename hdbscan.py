# hdbscan_clustering.py
import hdbscan
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def hdbscan_clustering(data, min_cluster_size_range, min_samples_range):
    best_min_cluster_size = None
    best_min_samples = None
    best_score = -1
    best_labels=None

    for min_cluster_size in min_cluster_size_range:
        for min_samples in min_samples_range:
            clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, min_samples=min_samples)
            labels = clusterer.fit_predict(data)

            if len(set(labels)) > 1 and len(set(labels)) < len(data):
                filtered_data = data[labels != -1]
                filtered_labels = labels[labels != -1]

                if len(set(filtered_labels)) >= 2:
                    score = silhouette_score(filtered_data, filtered_labels)
                    if score > best_score:
                        best_min_cluster_size = min_cluster_size
                        best_min_samples = min_samples
                        best_score = score
                        best_labels=labels

    return best_min_cluster_size, best_min_samples, best_score, best_labels

def visualize_hdbscan(data, labels):
    plt.figure(figsize=(10, 7))
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=50, edgecolor='k', alpha=0.7)
    plt.title('HDBSCAN Clustering')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Cluster Labels')
    plt.show()
