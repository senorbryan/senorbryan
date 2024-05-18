def search():
        print("Please input an ingredient to search:")
        ingredient = input()

        if ingredient in inventory:
                print("The supermarket supplies " + ingredient + ".")
        
        else:
                print("The supermarket does not supply " + ingredient + ".")
        

def sort(inventory):
        print("Are you sure you want to alphabetize the inventory? This cannot be undone.")
        print("1. Yes")
        print("2. No")
        
        choice = input()

        if (choice == '1'):
            inventory.sort()

        print("Here is the alphabetized list:")
        print()
        print("**Options**")

        for i,item in enumerate(inventory, 1):
                    print(i, item)

        else:
            pass

def delete():
        print("Input the ingredient you would like to delete:")
        ingredient = input()

        if ingredient in inventory:
            inventory.remove(ingredient)
            print("The ingredient " + ingredient + " has been removed")

        else:
            print("The ingredient " + ingredient + " is not in our inventory.")
        

choice = ''
inventory = ["Potato", "Cauliflower", "Shrimp", "Crab", "Chorizo", 
        "Scallop", "Corn"]

print("Michelin Star Inc. welcomes you, our esteemed food critic, to manage our produce inventory.")
print("Please feel free to modify the list in any way you desire.")
print()
print("**Options**")

for i,item in enumerate(inventory, 1):
            print(i, item)


while not(choice == '4'):
        print("--Actions--")
        print("1. Search for a side dish")
        print("2. Alphabetize the list")
        print("3. Delete a side dish")
        print("4. Submit List")

        choice = input()

        if (choice == '1'):
                search()
                choice == ''

        if (choice == '2'):
                sort(inventory)
                choice == ''


        if (choice == '3'):
                delete()
                pass
                choice == ''

        if (choice == '4'):
                break;


print("Here is the finalized list. Thank you esteemed critic.")
print()

for i,item in enumerate(inventory, 1):
            print(i, item)

