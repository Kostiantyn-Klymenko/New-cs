class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says Meow!")

    def change_name(self, new_name):
        self.name = new_name



c1 = Cat("Whiskers") # instance of Cat class
c2 = Cat("Mittens") # another instance of Cat class

c2.meow() # Output: Whiskers says Meow!
