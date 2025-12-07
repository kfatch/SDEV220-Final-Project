#Kody Fatch
#SDEV220 Final Project - Managment App for Clay County Humane Society. Purpose of app is to manage inventory, handle animal information, intake and adoption, and track profit/expenses.Sf

# class Animal():
#     def __init__(self, sex, age, color, name):
#         self.sex = sex
#         self.age = age
#         self.color = color
#         self.name = name
# class Cat(Animal):
#     def __init__(self, sex, age, color, name, declawed, FEV):
#         super().__init__(sex)
#         super().__init__(age)
#         super().__init__(color)
#         super().__init__(name)
#         self.declawed = declawed
#         self.FEV = FEV
# class Dog(Animal):
#     def __init__(self, sex, age, color, name):
#         super().__init__(sex)
#         super().__init__(age)
#         super().__init__(color)
#         super().__init__(name)
# class Inventory():
#     def __init__(self, food, bed):
#         self.food = food
#         self.bed = bed
# class CatInv(Inventory):
#     super().__init__(food)
#     super().__init__(bed)
# class DogInv(Inventory):
#     super().__init__(food)
#     super().__init__(bed)
def print_menu():
    print("Animal Management:    1")
    print("Inventory Management: 2")
    print("Revenue Management:   3")
    print("Quit:                 0")
def animal_menu():
    print("Add animal:       1")
    print("Delete animal:    2")
    print("Show Animal List: 3")
    print("Go Back:          4")
    print("Quit:             0")
def inventory_menu(): 
    print("Add Item to Order List:         1")
    print("Remove Item from Order List:    2")
    print("Complete List and Submit Order: 3")
    print("Go Back:                        4")
    print("Quit:                           0")
def revenue_menu():
    print("Add Profit:     1")
    print("Add Expense:    2")
    print("Change a Value: 3")
    print("Go Back:        4")
    print("Quit:           0")

menu_lvl = 0
print("Welcome to Clay County Humane Society Management System.")
print_menu()
user_input = int(input("Select A Number To Proceed.\n"))
while (user_input < 0) or (user_input > 4):
    user_input = int(input("Enter a valid option.\n"))
else:
    while (user_input != 0):
        pass