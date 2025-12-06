#Kody Fatch
#SDEV220 Final Project - Managment App for Clay County Humane Society. Purpose of app is to manage inventory, handle animal information, intake and adoption, and track revenue.

class Animal():
    def __init__(self, sex, age, color, name):
        self.sex = sex
        self.age = age
        self.color = color
        self.name = name
class Cat(Animal):
    def __init__(self, sex, age, color, name, declawed, FEV):
        super().__init__(sex)
        super().__init__(age)
        super().__init__(color)
        super().__init__(name)
        self.declawed = declawed
        self.FEV = FEV
class Dog(Animal):
    def __init__(self, sex, age, color, name):
        super().__init__(sex)
        super().__init__(age)
        super().__init__(color)
        super().__init__(name)
def print_menu():
    print("Select A Number To Proceed.")
    print("Animal Management:    1")
    print("Inventory Management: 2")
    print("Revenue Management:   3")

print("Welcome to Clay County Humane Society Management System.")
print_menu()