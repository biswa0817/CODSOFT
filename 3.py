import numpy as np
from scipy.sparse.linalg import svds

# Load user-movie rating matrix
R = np.array([
    [4, 3, 5, 2, 1],
    [3, 4, 2, 5, 3],
    [5, 2, 4, 3, 2],
    [2, 5, 3, 4, 1],
    [1, 3, 2, 5, 4]
])

# Perform matrix factorization using SVD
U, sigma, Vt = svds(R, k=2)

# Compute user latent factors
U = U * sigma

# Compute movie latent factors
V = Vt.T

# Compute predicted ratings
predicted_ratings = np.dot(U, V.T)

# Print predicted ratings
print(predicted_ratings)
# Compute dot product of user 1's latent factors with movie latent factors
scores = np.dot(U[0], V.T)
# Print scores
print(scores)
from sklearn.neighbors import NearestNeighbors

# Load user-movie rating matrix
R = np.array([
    [4, 3, 5, 2, 1],
    [3, 4, 2, 5, 3],
    [5, 2, 4, 3, 2],
    [2, 5, 3, 4, 1],
    [1, 3, 2, 5, 4]
])

# Create nearest neighbors model
nn = NearestNeighbors(n_neighbors=2)

# Fit model to user-movie rating matrix
nn.fit(R)

# Compute nearest neighbors for user 1
distances, indices = nn.kneighbors(R[0].reshape(1, -1))

# Print nearest neighbors
print(indices)