![download](https://github.com/user-attachments/assets/ae60e20f-23c7-496d-94da-143a9f045450)# Clustering Analysis Project

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
- Optimal “k”: **(48)**
- Silhouette Score: **(0.5942)**
- ![download](https://github.com/user-attachments/assets/f128afc0-7bf4-4f8b-b5d3-381810e0af11)


### DBSCAN
- Best Parameters: **eps = (0.1)**, **min_samples = (45)**
- Silhouette Score: **(0.6700)**
- ![download](https://github.com/user-attachments/assets/ea766b30-189e-46c9-ab82-0548d1bffeb7)


### HDBSCAN
- Best Parameters: **min_cluster_size = (45)**, **min_samples = (45)**
- Silhouette Score: **(0.8471)**
- ![download](https://github.com/user-attachments/assets/b45ac935-bdf2-4974-b3da-410d722b37e6)


### Hierarchical Clustering
- Optimal Number of Clusters: **(49)**
- Silhouette Score: **(0.5914)**
- ![download](https://github.com/user-attachments/assets/2c33b69f-dd55-4175-a7f9-1890dc340582)

While the Silhouette Scores for DBSCAN (0.6700) and HDBSCAN (0.8471) are higher compared to K-Means (0.5942) and Hierarchical Clustering (0.5914), it is important to consider the proportion of points classified as noise by DBSCAN and HDBSCAN.

Both DBSCAN and HDBSCAN classify a significant portion of the data points as noise, which can lead to a misleadingly high Silhouette Score. This happens because the score is calculated only on the remaining clustered points, which may exhibit high intra-cluster similarity. However, this approach might overlook valuable insights about the full dataset.

In contrast, K-Means, with an optimal "k" of 48, successfully clusters the entire dataset without discarding any points as noise. Although its Silhouette Score is slightly lower, it provides a more comprehensive clustering solution that considers all the data points, making it the better choice for this specific dataset.

Thus, K-Means is deemed the preferred clustering method in this case, balancing interpretability, completeness, and utility.

---

## Files and Structure
1. **`requirements.txt`**: Contains all dependencies required for the project.
2. **`dataclean.py`**: Handles data loading, cleaning, and scaling.
3. **`kmeans.py`**: Implements K-Means clustering and visualizations.
4. **`dbscan.py`**: Implements DBSCAN clustering and visualizations.
5. **`hdbscan_clustering.py`**: Implements HDBSCAN clustering and visualizations.
6. **`hierarchical_clustering.py`**: Implements hierarchical clustering and visualizations.
7. **`run_clustering.py`**: The main script to execute all clustering methods sequentially.




