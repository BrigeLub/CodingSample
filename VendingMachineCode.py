# Purpose: Vending Machine Program
# Author: Brigitte Lubker
# Date: 4/29/22


# Display Menu
print("Vending Machine\n")
print("1. Roasted Almonds --> $1.25")
print("2. Pretzels        --> $1.75")
print("3. Chewing Gum     --> $0.90")
print("4. Mints           --> $0.75")
print("5. Chocolate bar   --> $1.50")
print("6. Cookies         --> $2.00\n")

#dictionary for referencing user selection
guide = {1: 1.25, 2: 1.75, 3: 0.90, 4: 0.75, 5: 1.50, 6: 2.00}
menu = {1:"Roasted Almonds",2:"Pretzels",3:"Chewing Gum",4:"Mints",5:"Chocolate bar",6:"Cookies"}

# Get and validate user input:
button = input("Enter your choice of item: ")

try:
    button = int(button)
except:
    print("Value entered was not a number.")
    quit()
try:
    selection = guide[button]
    #print(selection)
except:
    print("Invalid item choice.")
    quit()

#dealing with price
money = input("Enter money to purchase item: ")

try:
    money = float(money)
except:
    print("Value entered was not a number.")
    quit()
if money < 0:
    print("Amount of money cannot be a negative value.")
    quit()
difference = money-selection
#print(difference)
if money >= guide[button]:
    print("Thanks for buying "+menu[button]+".")
    print("Your change is ${0:.2f}.".format(difference))
    
if money < selection:
    print("You are ${0:.2f} short.".format(abs(difference)))
    quit()