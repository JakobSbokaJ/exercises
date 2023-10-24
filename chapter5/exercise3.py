import random

money = random.randint(0,5000)

print(money)
if money > 100 and money < 500:
    print("Between 100 and 500")
elif money > 1000 and money < 5000:
    print("Between 1000 and 5000")
else:
    print("Not between 100 and 500 or 1000 and 5000")