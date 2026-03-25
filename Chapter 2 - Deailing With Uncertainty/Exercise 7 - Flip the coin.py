import random

def flip_coin():
    if random.random() < 0.5:
        return "HEADS"
    else:
        return "TAILS"

heads = 0
tails = 0

for i in range(100):
    result = flip_coin()
    if result == "HEADS":
        heads += 1
    else:
        tails += 1

print("HEADS", heads)
print("TAILS", tails)