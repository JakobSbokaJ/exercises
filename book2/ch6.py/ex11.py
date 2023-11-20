cities = {
    "new york city":{
        'country':"america",
        'population':"8.5 million",
        'fact':"the first pizzeria in the United States was opened in NYC in 1905"
    },
    "rio de janeiro":{
        'country':"brazil",
        'population':"6.75 million",
        'fact':"it has the 8th biggest library in the world"
    },
    "sydney":{
        'country':"australia",
        'population':"5.3 million",
        'fact':"it has over 100 beaches"
    }
}

for city, stuff in cities.items():
    print(f"{city.title()} is in {stuff['country'].title()}. It has a population of {stuff['population']}. \nA random fact about it is that {stuff['fact']}.\n")