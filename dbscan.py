# dbscan.py
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

def dbscan_clustering(data, eps_range, min_samples_range):
    best_eps = None
    best_min_samples = None
    best_score = -1

    for eps in eps_range:
        for min_samples in min_samples_range:
            dbscan = DBSCAN(eps=eps, min_samples=min_samples)
            labels = dbscan.fit_predict(data)

            if len(set(labels)) > 1 and len(set(labels)) < len(data):
                filtered_data = data[labels != -1]
                filtered_labels = labels[labels != -1]

                if len(set(filtered_labels)) >= 2:
                    score = silhouette_score(filtered_data, filtered_labels)
                    if score > best_score:
                        best_eps = eps
                        best_min_samples = min_samples
                        best_score = score
    
    return best_eps, best_min_samples, best_score

def visualize_dbscan(data, labels):
    unique_labels = set(labels)
    plt.figure(figsize=(8, 6))
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
    for label, color in zip(unique_labels, colors):
        if label == -1:
            color = [0, 0, 0, 1]
        mask = (labels == label)
        plt.scatter(data[mask, 0], data[mask, 1], c=[color], marker='o', alpha=0.7, edgecolor='k')
    plt.title('DBSCAN Clustering')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
