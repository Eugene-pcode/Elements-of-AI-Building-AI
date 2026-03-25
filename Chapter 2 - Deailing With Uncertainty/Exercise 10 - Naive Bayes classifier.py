import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

def bayes(sequence):
    odds = 1.0           # start with odds 1:1 (equal prior probability)
    for roll in sequence:
        if roll == 6:
            # P(6 | loaded) / P(6 | normal) = 0.5 / (1/6) = 3
            r = 0.5 / (1/6)
        else:
            # P(non-6 | loaded) / P(non-6 | normal) = 0.1 / (1/6) = 0.6
            r = 0.1 / (1/6)
        odds = odds * r
    # Return True if odds > 1 (loaded more likely)
    return odds > 1

# Test with a loaded die
sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")