#modified ex 4

nums = []

for i in range(1,1000001):
    nums.append(i)
print(nums)

#modified ex 9

nums = [num**3 for num in range(1,11)]
print(nums)

#modified ex 13

buffetFoods = ["chicken", "steak", "turkey", "scallop", "onion"]

for food in buffetFoods:
    print(f"This restaurant serves {food}.")

buffetFoods[1] = "burger"
buffetFoods[4] = "macncheese"

print("Menu update!")
for food in buffetFoods:
    print(f"Item: {food}")