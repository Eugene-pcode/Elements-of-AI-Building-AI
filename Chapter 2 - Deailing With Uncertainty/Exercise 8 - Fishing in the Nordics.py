countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # Calculate total population and total fishers
    total_population = sum(populations)
    total_fishers = sum(fishers)
    
    # Find country with highest probability
    best_prob = 0
    best_country = ""
    
    for i in range(len(countries)):
        # P(country | fisher) = P(fisher | country) * P(country) / P(fisher)
        # P(fisher | country) = fishers[i] / populations[i]
        # P(country) = populations[i] / total_population
        # P(fisher) = total_fishers / total_population
        # Simplified: P(country | fisher) = fishers[i] / total_fishers
        prob = fishers[i] / total_fishers * 100
    
        if prob > best_prob:
            best_prob = prob
            best_country = countries[i]
    
    return (best_country, best_prob)

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()