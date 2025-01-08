# kmeans.py
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def kmeans_clustering(data, max_clusters=50):
    best_k = None
    best_score = -1
    for k in range(2, max_clusters):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        labels = kmeans.labels_

        if len(set(labels)) > 1 and len(set(labels)) < len(data):
            score = silhouette_score(data, labels)
            if score > best_score:
                best_k = k
                best_score = score
    
    return best_k, best_score

def visualize_kmeans(data, labels, centroids):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o', alpha=0.7, edgecolor='k')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', label='Centroids', marker='X')
    plt.title('K-Means Clustering')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()
