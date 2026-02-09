#shopping list app

shoppingList = []

def showMenu():
    print("\nChoose the menu")
    print("1. See your shopping list")
    print("2. Add an item")
    print("3. Remove an item ")
    print("4. Edit your shopping list")
    print("5. Clear your shopping list")
    print("6. Exit")

while True:
    showMenu()
    choice = input("input your choice (1-6): ")
    
    if choice == "1":
        print("-Your Shopping List-")
        if not shoppingList:
            print("your shopping list is empty")
        else :
            for index,item in enumerate(shoppingList):
                print(f"{index + 1} . {item}")
    elif choice == "2":
        item = input("enter the item to add: ")
        shoppingList.append(item)
        print(f"{item} has been added to your list")
    elif choice == "3":
        item = input("enter the item to remove: ")
        if item in shoppingList:
            shoppingList.remove(item)
            print(f"{item} has been removed from your list")
        else:
            print(f"{item} is not in your shopping list")
    elif choice == "4":
        item = input("which item you want to edit: ")
        if item in shoppingList:
            shoppingList.remove(item)
            new_item = input("what item do you want add: ")
            shoppingList.append(new_item)
        else: 
            print(f"{item} is not in your shopping list")
    elif choice == "5":
        shoppingList.clear()
        print("Now your list is empty!")
    elif choice == "6":
        print("GoodBye!!")
        break
    else:
        print("Choose the right number")

with open("project-007/list.txt", "w", encoding="utf-8") as f:
    for item in shoppingList:
        f.write(item + "\n")