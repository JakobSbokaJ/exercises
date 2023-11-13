import random

twinkies = random.randint(0,1000)

print(twinkies)

if twinkies < 100:
    print("Too few")
elif twinkies > 500:
    print("Too many")
