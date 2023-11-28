class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"""Welcome to {self.restaurant_name.title()}!
We serve {self.cuisine_type.title()} cuisine!""")

    def open_restaurant(self):
        print("We are now open!!")

restaurant1 = Restaurant("greasy grove","american")
restaurant2 = Restaurant("tomato temple","italian")
restaurant3 = Restaurant("Pizza Pit","also italian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()