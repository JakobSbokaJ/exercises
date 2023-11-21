country = "America"
def describe_city(city,country):
    if country:
        print(f"{city} is in {country}.")
    else: 
        print(f"{city} is in America.")

describe_city("NYC", "")
describe_city("Rio de Janeiro", "Brazil")
describe_city("Moscow", "Russia")