cities = []

while True:
    city = input("Input a city name! Input 'done' to end. ")
    if city == "done":
        break
    else:
        cities.append(city)

for city in cities:
    print(f"{city} is a cool city.")