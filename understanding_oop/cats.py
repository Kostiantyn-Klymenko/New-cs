class Cat:
    def __init__(self, name,age, status):
        self.name = name
        self.age = age
        self.status = status

    def tell_what_cat_doing(self):
        return f"{self.name} is {self.status} and is {self.age} years old."
    def change_status(self, new_status):
        self.status = new_status
        return f"{self.name} is now {self.status}."