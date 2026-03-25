import numpy as np

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)  # Fixed: np.float → float
    
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i, j] = np.inf
            else:
                dist[i, j] = np.sqrt(np.sum((data[i] - data[j])**2))
    
    # Find the pair with smallest distance
    min_dist = np.min(dist)
    min_idx = np.unravel_index(np.argmin(dist), dist.shape)
    
    return min_idx, min_dist

# Example usage
data = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
idx, d = find_nearest_pair(data)
print(f"Nearest pair: {idx}, distance: {d}")
