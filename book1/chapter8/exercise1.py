class Thing:
    pass

class Animate(Thing):
    pass

class Animal(Animate):
    def move(self):
        print("moving")
    def breathe(self):
        print("breathing")
    def eat_food(self):
        print("eating")

class Mammal(Animal):
    def feed_young_with_milk(self):
        print("feeding")

class Giraffe(Mammal):
    def eat_leaves_from_trees(self):
        print("tearing a leaf")
        self.eat_food
    def left_foot_forward(self):
        print("left foot forward")
    def left_foot_back(self):
        print("left foot backward")
    def right_foot_forward(self):
        print("right foot forward")
    def right_foot_back(self):
        print("right foot backward")
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()

reginald = Giraffe()
reginald.eat_leaves_from_trees()
reginald.dance()