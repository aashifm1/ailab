import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture 
np.random.seed(0)
n_samples = 300
X1 = np.random.randn(n_samples, 2) + np.array([5, 5]) 
X2 = np.random.randn(n_samples, 2) + np.array([-5, -5]) 
X = np.vstack((X1, X2))
n_components = 2
gmm = GaussianMixture(n_components=n_components) 
gmm.fit(X)
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=50)
plt.title('EM Clustering using Gaussian Mixture Model') 
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid()
plt.show()