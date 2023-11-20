cities = []
baller = True

while baller:
    city = input("Input a city name! Input 'done' to end. ")
    if city == "done":
        baller = False
    else:
        cities.append(city)

for city in cities:
    print(f"{city} is a cool city.")