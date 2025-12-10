#Kody Fatch
#SDEV220 Final Project - Managment App for Clay County Humane Society. Purpose of app is to manage inventory, handle animal information, intake and adoption, and track profit/expenses.

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
    print("Show Inventory List:            3")
    print("Go Back:                        4")
    print("Quit:                           0")
def revenue_menu():
    print("Add Profit:     1")
    print("Add Expense:    2")
    print("Change a Value: 3")
    print("Go Back:        4")
    print("Quit:           0")

menu_lvl = 0    #Used for identify which menu the user is currently in. 0 for main(entry level), 1 for in a menu one level deep, etc
menu_id = 0    #Used to identify which submenu the user is in. (0 for Main, 1 for Animal, 2 for Inventory, and 3 for Revenue)

print("Welcome to Clay County Humane Society Management System.")
print_menu()
user_input = int(input("Select A Number To Proceed.\n"))
while (user_input < 0) or (user_input > 3):
    user_input = int(input("Enter a valid option.\n"))
menu_lvl += 1
while (user_input != 0):
    while (menu_lvl > -1) and (menu_lvl < 3):
        while menu_lvl == 1:
            if user_input == 1:
                animal_menu()
                user_input = int(input("Select A Number To Proceed.\n"))
                if (user_input > 0) and (user_input < 4):
                    menu_lvl += 1
                else:
                    menu_lvl -= 1
            elif user_input == 2:
                inventory_menu()
                user_input = int(input("Select A Number To Proceed.\n"))
                if (user_input > 0) and (user_input < 4):
                    menu_lvl += 1
                else:
                    menu_lvl -= 1
            elif user_input == 3:
                revenue_menu()
                user_input = int(input("Select A Number To Proceed.\n"))
                if (user_input > 0) and (user_input < 4):
                    menu_lvl += 1
                else:
                    menu_lvl -= 1
        while menu_lvl == 0:
            print_menu()
            user_input = int(input("Select A Number To Proceed.\n"))
            while (user_input < 0) or (user_input > 3):
                user_input = int(input("Enter a valid option.\n"))
            menu_lvl += 1
        while menu_lvl == 2:
            pass