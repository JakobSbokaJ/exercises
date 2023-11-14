buffetFoods = ["chicken", "steak", "turkey", "scallop", "onion"]

for food in buffetFoods:
    print(f"This restaurant serves {food}.")

buffetFoods[1] = "burger"
buffetFoods[4] = "macncheese"

print("Menu update!")
for food in buffetFoods:
    print(f"Item: {food}")