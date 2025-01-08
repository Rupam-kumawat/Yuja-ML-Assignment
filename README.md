# Clustering Analysis Project

## Overview
This project demonstrates various clustering techniques applied to geospatial data using Python. The dataset contains longitude and latitude coordinates, and the goal is to explore the clustering structure and identify groups within the data. The clustering methods implemented include:

1. **K-Means Clustering**
2. **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise)
3. **HDBSCAN** (Hierarchical DBSCAN)
4. **Hierarchical Clustering**

The project is divided into modular scripts for clarity and scalability, enabling efficient experimentation with different clustering techniques.

---

## Approach

### Data Cleaning
1. **Loading Data**: The dataset was imported as a CSV file.
2. **Parsing Coordinates**: Longitude and Latitude were extracted from a combined field.
3. **Handling Missing/Invalid Data**: Non-numeric entries were converted, and rows with invalid or duplicate data were removed.

### Data Scaling
The dataset was standardized using `StandardScaler` from `sklearn` to ensure uniformity across clustering methods, as many algorithms are sensitive to feature scales.

### Clustering Methods
#### 1. K-Means Clustering
- A grid search approach was employed to determine the optimal number of clusters (“k”).
- The evaluation was based on the **Silhouette Score**, which measures the separation and cohesion of clusters.
- Centroids were visualized to interpret cluster centers.

#### 2. DBSCAN
- Parameters “eps” (neighborhood radius) and “min_samples” (minimum points for a cluster) were tuned using grid search.
- Models with only noise or a single cluster were ignored.
- Results were evaluated using the Silhouette Score.

#### 3. HDBSCAN
- This extended DBSCAN by dynamically adjusting “eps” and generating hierarchical clusters.
- Parameters “min_cluster_size” and “min_samples” were optimized for the best clustering performance.

#### 4. Hierarchical Clustering
- The number of clusters was determined by iterating over a range and evaluating Silhouette Scores.
- Linkage criteria: Ward’s method, which minimizes variance within clusters.

### Visualization
Each method's results were visualized using scatter plots, with colors representing different clusters. Noise points (if any) were highlighted distinctly.

---

## Assumptions
1. Data points are homogeneously distributed without any significant missing data after cleaning.
2. Clusters in the dataset have a spatial structure that can be captured by distance-based algorithms.
3. Silhouette Score is an adequate metric for clustering evaluation given the two-dimensional data.

---

## Hurdles
1. **Parameter Tuning**: Finding optimal values for DBSCAN and HDBSCAN required significant computational time due to exhaustive grid search.
2. **Noisy Data**: Initial datasets contained several noise points, making clustering results less interpretable.
3. **Cluster Validation**: Evaluating clustering performance using Silhouette Scores sometimes penalized valid clusters with elongated or irregular shapes.

---

## Solution
- Efficient grid search mechanisms and smaller parameter ranges were used to reduce computational load.
- Noise points were explicitly handled and excluded during evaluation for DBSCAN and HDBSCAN.
- Visual validation of clusters supplemented metric-based evaluation to ensure practical relevance.

---

## Results
### K-Means
- Optimal “k”: **(varies per run)**
- Silhouette Score: **(varies per run)**

### DBSCAN
- Best Parameters: **eps = (value)**, **min_samples = (value)**
- Silhouette Score: **(value)**

### HDBSCAN
- Best Parameters: **min_cluster_size = (value)**, **min_samples = (value)**
- Silhouette Score: **(value)**

### Hierarchical Clustering
- Optimal Number of Clusters: **(value)**
- Silhouette Score: **(value)**

---

## Files and Structure
1. **`requirements.txt`**: Contains all dependencies required for the project.
2. **`dataclean.py`**: Handles data loading, cleaning, and scaling.
3. **`kmeans.py`**: Implements K-Means clustering and visualizations.
4. **`dbscan.py`**: Implements DBSCAN clustering and visualizations.
5. **`hdbscan_clustering.py`**: Implements HDBSCAN clustering and visualizations.
6. **`hierarchical_clustering.py`**: Implements hierarchical clustering and visualizations.
7. **`run_clustering.py`**: The main script to execute all clustering methods sequentially.




