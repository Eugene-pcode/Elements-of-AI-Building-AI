import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(coeff):
    # Calculate the dot product: z = coeff · x
    z = np.dot(coeff, x)
    
    # Apply sigmoid function: σ(z) = 1 / (1 + e^(-z))
    result = 1 / (1 + math.exp(-z))
    
    return result

# Calculate the output of the sigmoid for x with all three coefficients
print("Sigmoid for c1:", sigmoid(c1))
print("Sigmoid for c2:", sigmoid(c2))
print("Sigmoid for c3:", sigmoid(c3))