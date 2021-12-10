'''Copyright (c) 2021 AIClub
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without 
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, subject to the following 
conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.'''

# Python program to generate random data in 2D and run k means algorithm on the dataset.

# Import pyplot to plot the graphs
import matplotlib.pyplot as plt

# Import make_blobs to generate two dimensional dataset
from sklearn.datasets import make_blobs

# Import kmeans module
from sklearn.cluster import KMeans

# Import silhouette_score function
from sklearn.metrics import silhouette_score

# ------------------------------------ Generate and plot the 2D dataset -------------------------------------------

# Generate the two dimensional dataset
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=0)

# Plot the dataset figure
plt.scatter(X[:, 0], X[:, 1], s=50)

# Show the random dataset figure
plt.show()

# ----------------------------------- Run k-means algorithm and plot the clusters ----------------------------------

# Mention the generated number of clusters and initialize the model
kmeans = KMeans(n_clusters=4)

# Train kmeans model
kmeans.fit(X)

# Predict the closest cluster
y_kmeans = kmeans.predict(X)

# Plot the clusters
# Map each cluster to a different color using cmap
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Get coordinates of cluster centers
centers = kmeans.cluster_centers_

# Plot the centers
# Centroid color is black
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200)

# Show the clusters with their centroids
plt.show()

# --------------------------------------- Calculate the Silhoutte Score  --------------------------------------------

# Calculate Silhoutte Score
silhoutte_score = silhouette_score(X, kmeans.labels_, metric='euclidean')

# Print the Silhoutte score
print ('Silhouetter Score:', silhoutte_score)




