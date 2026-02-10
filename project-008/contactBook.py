#contact book program with python
contact = {}

def contactMenu():
    print("\n-contact books menu-")
    print("1. Show contact")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Remove contact")
    print("6. Exit")
    
    
def addContact():
    name = input("input your name: ")
    phone = input("input your phone number: ")
    email = input("input your email: ")
    
    contact[name] = {"phone": phone, "email" : email}
    print(f"contact name as {name} has been added to contact book")
    print(contact)

def viewContact():
    if contact:
        print("\n-contact list-")
        for name, details in contact.items():
            print(f"Name : {name}")
            print(f"Phone : {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("your contact book is empty")

def searchContact():
    name = input("input the name on the contact you want to search: ")
    if name in contact:
        print(f"-contact details of {name}-")
        print(f"Name: {name}")
        print(f"Email: {contact[name]['email']}")
        print(f"Phone: {contact[name]['phone']}")
    else:
        print("Contact doesn't exist")

def editContact():
    name = input("input the name of the contact that you want to edit: ")
    if name in contact:
        phone = input("input new phone number: ")
        email = input("input new email: ")
        contact[name] = {'phone': phone, 'email' : email}
        print(f"contact {name} has been updated sucessfully")
    else:
        print("Contact doesn't exist")

def deleteContact():
    name = input("input contact name that you want to delete: ")
    if name in contact:
        del contact[name]
        print("contact has been deleted")
    else:
        print("Contact doesn't exist")
        
while True:
    contactMenu()
    choice = input("choose the menu (1-6): ")
    try:
        if choice == '1':
            viewContact()
        elif choice == '2':
            addContact()
        elif choice == '3':
            searchContact()
        elif choice == '4':
            editContact()
        elif choice == '5':
            deleteContact()
        elif choice == '6':
            print("Thank you for using this application goodbye!! ")
            break
        else:
            print("please choose the right number (1-6)")
    except ValueError:
        print("please do a valid input")
        
with open("project-008/contact.txt", "w", encoding="utf-8") as f:
    for name, details in contact.items():
        f.write(
            f"Name : {name}, "
            f"Email : {details['email']}, "
            f"Phone : {details['phone']}\n"
        )
    