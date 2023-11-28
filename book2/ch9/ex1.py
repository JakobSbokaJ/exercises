class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"""Welcome to {restaurant_name.title()}!
        We serve {cuisine_type} cuisine!""")

    def open_restaurant(self):
        print("We are now open!!")

restaurant = Restaurant("m is zesty","lemons")
print(f"The restaurant name is {restaurant.restaurant_name.title()}, and the cuisine is {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()