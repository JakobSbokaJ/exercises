def describe_city(city,country="America"):
    if country:
        print(f"{city} is in {country}.")
    else: 
        print(f"{city} is in {country}.")

describe_city("NYC")
describe_city("Rio de Janeiro", "Brazil")
describe_city("Moscow", "Russia")