#building note taking app project

#define files to open the files
FILE_NAME = "project-010/notes.txt"

def showMenu():
    #function for app menu
    print("\n-Note Taking App Menu-")
    print("1. Add note")
    print("2. View note")
    print("3. Delete note")
    print("4. Exit")

def addNote():
    #function for adding notes
    add_content = input("input your notes content: ")
    with open(FILE_NAME, 'a') as file:
        file.write(add_content + "\n")
        print("notes added succesfully")

def viewNote():
    #function for viewing notes
    try:
        with open(FILE_NAME, 'r') as file:
            content = file.read()
            if content:
                print("\n~Your Notes~")
                print(content)
            else:
                print("There is no content in your notes")
    except FileNotFoundError:
        print("file can't be found")
        
def deleteNote():
    #function for deleting all content inside notes
    checking = input("are you sure to delete all content (Yes/n): ")
    if checking.lower() == "yes":
        with open(FILE_NAME,'w') as file:
            pass
        print("all  notes has been deleted")
    else:
        print('deletion cancelled')

while True:
    showMenu()
    choice = input("enter your choice (1-4): ")
    if choice == "1":
        addNote()
    elif choice == "2":
        viewNote()
    elif choice == "3":
        deleteNote()
    elif choice == "4":
        break
    else:
        print("please input the right choice")
        
    