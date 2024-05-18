#Assignment 4 - Data Structures and Lists

#Array containing wholesaler inventory
inventory = ["Atorvastatin" , "Amoxicillin", "Escitalopram", "Guaifenesin", "Hydrochlortiazide", "Icosapent", "Kerendia", "Lorazepam", "Metoprolol", "Nifedipine", "Omeprazole",
             "Quetiapine", "Risperidone", "Sertraline", "Tramadol", "Ubrevly", "Vilazodone", "Wegovy", "Xigduo", "Yasmin", "Zolpidem"]

#Array that will hold shopping cart items
cart = []
key = ""

#Specific key for the checkout option
checkout = ""

#Specific condition for the quit option
def quit():
    return False

#Introduction
print('Welcome to Kinray Inc. Please select your product:')
#for i, item in enumerate(inventory, 1):
    #print("#{1} {0}".format(item, i))

#Prints the inventory
for i,item in enumerate(inventory, 1):
    print(i, item)

#Fixes the index of choice for the user 
option = int(input())
option = option - 1

#Forces the user to pick within the length of the inventory size
while (option < 0 or option >= 22):
    print('You have inputted an invalid selection. Please select your product:')

    for i,item in enumerate(inventory, 1):
        print(i, item)
    option = int(input())

#Adds item to shopping cart
cart.append(inventory[option])

print("Shopping Cart:")

for (i,item) in enumerate(cart):
        print(i + 1, item)

print()

#Loop with commands for shopping cart, checking out, and quitting
while not(key == "quit"):
    print('Please enter a command:')
    print('1. [spacebar] to add an item to your cart')
    print('2. "-" or "Delete Item" to delete an item from your cart')
    print('3. "Reset" or "Restart" to empty cart and start over')
    print('4. "Checkout" to purchase items')
    print('5. "Quit" to close Kinray Inc.')

    key = input()
    key.lower()

    #Alphabetizes the array
    cart.sort()

    #Add command
    if (key == " " or key == "1"):
        print('Please select your product:')

        for i,item in enumerate(inventory, 1):
            print(i, item)


        option = int(input())
        option = option - 1

        while (option < 0 or option >= 22):
            print('You have inputted an invalid selection. Please select your product:')

            for i,item in enumerate(inventory, 1):
                print(i, item)
                option = int(input())

        cart.append(inventory[option])
        cart.sort()

        print("Shopping Cart:")

        for (i,item) in enumerate(cart):
            print(i + 1, item)

        print()
    
    #Subtract command
    elif (key == "-" or key == "delete item" or key == "2"):
        if not (cart):
            print("Your shopping cart is empty. There is nothing to subtract.")
        else:
            print("Please select an item to delete:")
            print()
            print("Shopping Cart:")

            for (i,item) in enumerate(cart):
                print(i + 1, item)

            item = int(input())
            item = item - 1
            while (item > len(cart)):
                print("Your input is invalid. Please select an item to delete:")
                for (i,item) in enumerate(cart):
                    print(i + 1, item)

            #Subtracts the item from the input that the user desires
            cart.pop(item)

            if not (cart):
                print("Your shopping cart is empty.")
            else:
                for (i,item) in enumerate(cart):
                    print(i + 1, item)

        print()
    
    #Reset command
    elif (key == "reset" or key == "restart" or key == "3"):
        #Clears the cart
        cart.clear()
        print("You have selected the Reset option. Your cart has been emptied.")
        print()

    #Checkout command
    elif (key == "checkout" or key == '4'):
        print()
        print("Shopping Cart:")
        for (i,item) in enumerate(cart):
                print(i + 1, item)
        
        print()
        print('Enter "Y" or "Yes" to confirm:')
        checkout = input()

        if (checkout == "y" or checkout == "yes"): 
            #Exits the loop
            break
        else:
            continue

    #Quit option
    elif (key == "quit" or key == '5'):
        print("Thank you for choosing Kinray Inc. Until next time!")

        #Quit condition to avoid printing a checkout specific message
        quit() == True
        break
    else:
         print("You have not input any of the listed commands. Please try again.")

print()

if quit() == True:
    pass
else:       
    print('Thank you for choosing Kinray. Your invoice is listed below:')
    print()
    for (i,item) in enumerate(cart):
            print(i + 1, item)
         
         




