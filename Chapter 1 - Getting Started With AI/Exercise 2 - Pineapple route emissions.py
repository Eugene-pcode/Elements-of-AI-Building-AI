portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

smallest = 1000000
bestroute = [0, 0, 0, 0, 0]
D = [
    [0,8943,8019,3652,10545],
    [8943,0,2619,6317,2078],
    [8019,2619,0,5836,4939],
    [3652,6317,5836,0,7825],
    [10545,2078,4939,7825,0]
]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

def permutations(route, ports):
    global smallest, bestroute
    
    if len(ports) < 1:
        # Calculate total distance for this complete route
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += D[route[i]][route[i + 1]]
        
        # Check if this route is shorter than the best found so far
        if total_distance < smallest:
            smallest = total_distance
            bestroute = route.copy()
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i+1:])

def main():
    global smallest
    # Start from Helsinki (index 4) and visit all other ports
    permutations([4], list(range(4)))  # ports 0,1,2,3 are PAN, AMS, CAS, NYC
    
    # Calculate CO₂ emissions from the shortest distance
    emissions = smallest * co2
    
    # Print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % emissions)

main()