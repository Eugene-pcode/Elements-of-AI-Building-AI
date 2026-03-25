import random

def main():
    prob = random.random()
    if prob < 0.1:
        favourite = "bats"
    elif prob < 0.2:  # 0.1 <= prob < 0.2
        favourite = "cats"
    else:  # prob >= 0.2
        favourite = "dogs"
    # change this - now fixed with proper probability distribution
    print("I love " + favourite)

main()