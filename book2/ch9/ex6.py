class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"""Welcome to {self.restaurant_name.title()}!
We serve {self.cuisine_type.title()} cuisine!""")

    def open_restaurant(self):
        print("We are now open!!")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def displayFlavors(self):
        print(self.flavors)

flavorsList = ["korean bbq","sawdust","jakob schmierer","birfday"]
stand = IceCreamStand("creamy surprises","ice cream",flavorsList)
#I'm just going to call describe_restaurant to make sure it works
stand.describe_restaurant()
stand.displayFlavors()

    

    