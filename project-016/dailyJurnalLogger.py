filename= "project-016/journal.txt"

def addTopic():
    entry = input("enter your daily journal: ").lower()
    with open(filename,"a") as f:
        f.write(entry +"\n")
    print("daily journal has been added")

def viewTopic():
    with open(filename, "r") as f:
        content = f.read()
        if content:
            print("-Daily Jurnal Logger-")
            print(content)
        else:
            print("jurnal is empty")

def searchJournal():
    keyword = input("enter a keyword to search for: ")
    try:
        with open(filename,'r') as f:
            content = f.readlines()
            found = False
            print("-search result-")
            for entry in content:
                if keyword in entry:
                    print(entry.strip())
                    found = True
                if not found :
                    print("no matching for keywords")
    except FileNotFoundError:
        print("No, journal file found")

def showMenu():
    print("\n-Daily Journal Menu-")
    print("1. add journal")
    print("2. view journal")
    print("3. search journal")
    print("4. exit")

while True:
    showMenu()
    try:
        choice = input("input your choice (1/2/3/4): ")
        
        if choice == '1':
            addTopic()
        elif choice == '2':
            viewTopic()
        elif choice == '3':
            searchJournal()
        elif choice == '4':
            break
        else:
            print("please input the right choice")
    except Exception as e:
        print(e)