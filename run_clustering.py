# run_clustering.py
from dataclean import load_and_clean_data, scale_data
from kmeans import kmeans_clustering, visualize_kmeans
from dbscan import dbscan_clustering, visualize_dbscan
from hdbscan_clustering import hdbscan_clustering, visualize_hdbscan
from hierarchical_clustering import hierarchical_clustering, visualize_hierarchical

# Load and clean data
data_cleaned = load_and_clean_data('ML Assignment Dataset.csv')
data_cleaned_scaled = scale_data(data_cleaned)

# Run KMeans clustering
best_k, best_score = kmeans_clustering(data_cleaned_scaled)
print(f"KMeans - Best k: {best_k}, Best silhouette score: {best_score}")

# Run DBSCAN clustering
best_eps, best_min_samples, best_score = dbscan_clustering(data_cleaned_scaled, eps_range=np.arange(0.1, 1.0, 0.1), min_samples_range=range(3, 200, 4))
print(f"DBSCAN - Best eps: {best_eps}, Best min_samples: {best_min_samples}, Best silhouette score: {best_score}")

# Run HDBSCAN clustering
best_min_cluster_size, best_min_samples, best_score = hdbscan_clustering(data_cleaned_scaled, min_cluster_size_range=range(5, 100, 5), min_samples_range=range(5, 50, 5))
print(f"HDBSCAN - Best min_cluster_size: {best_min_cluster_size}, Best min_samples: {best_min_samples}, Best silhouette score: {best_score}")

# Run Hierarchical Clustering
best_n_clusters, best_score = hierarchical_clustering(data_cleaned_scaled)
print(f"Hierarchical - Best n_clusters: {best_n_clusters}, Best silhouette score: {best_score}")