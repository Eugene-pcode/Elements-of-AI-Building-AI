import numpy as np
import random

N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 50

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x
    global y

    for step in range(steps):
        # temperature schedule: starts high, decreases to 0
        T = max(0, ((steps - step)/steps)**3 - 0.005)
        
        # update solutions on each search track                                     
        for i in range(tracks):
            
            # try a new solution near the current one (within ±2 steps)                               
            x_new = np.random.randint(max(0, x[i]-2), min(N, x[i]+2+1))
            y_new = np.random.randint(max(0, y[i]-2), min(N, y[i]+2+1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # simulated annealing acceptance rule
            if S_new > S_old:
                # always accept better solutions
                x[i], y[i] = x_new, y_new
            else:
                # only consider worse solutions if T > 0
                if T > 0:
                    # accept worse solutions with probability exp(-ΔE / T)
                    if random.random() < np.exp(-(S_old - S_new) / T):
                        x[i], y[i] = x_new, y_new
                # if T == 0, do nothing (greedy behavior)
            
    # count how many tracks found the global peak
    found_peak = sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])
    print(f"Tracks that found the global peak: {found_peak} out of {tracks}")
    return found_peak

# run the simulation
result = main()