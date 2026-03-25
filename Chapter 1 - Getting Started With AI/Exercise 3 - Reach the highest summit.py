import math
import random

# generate random mountains
w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    path = [x]  # track the entire climbing path
    summit = False
    
    while not summit:
        summit = True
        
        # Check left and right
        for dx in [-1, 1]:
            neighbor = x + dx
            if 0 <= neighbor < len(h):
                if h[neighbor] > h[x]:
                    x = neighbor
                    path.append(x)  # record this step
                    summit = False
                    break  # found higher ground, continue climbing
    
    return x, path

def main(h):
    x0 = random.randint(1, 98)
    summit, path = climb(x0, h)
    return x0, summit, path

# Run the hill climbing
start, summit, path = main(h)

print(f"Started at position: {start}, height: {h[start]:.3f}")
print(f"Reached summit at position: {summit}, height: {h[summit]:.3f}")
print(f"Climbing path: {' → '.join(map(str, path))}")
print(f"Steps climbed: {len(path)-1}")

# Visualize with start (S), path (*), and summit (^)
print("\nMountain profile with climbing path:")
for i, height in enumerate(h):
    if i == start:
        marker = "S"  # Start position
    elif i == summit:
        marker = "^"  # Summit reached
    elif i in path[1:-1]:  # Intermediate positions (exclude start and summit)
        marker = "*"
    else:
        marker = "."
    bar = "█" * int(height * 20)
    print(f"{i:3d}: {marker} {bar} {height:.3f}")