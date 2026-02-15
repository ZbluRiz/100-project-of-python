#building a safe calculator with exception
filename = 'project-011/errorMessage.txt'
def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def substraction(a,b):
    return a - b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("cannot divided by zero")
    return a / b

def square(a,b):
    return a**b

def calculatorMenu():
    print("-safe calculator-")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Exit")
    
def valueErrorMsg():
    with open(filename, 'w') as file:
        file.write("invalid input , please enter the right input" + "\n")

def checkMsg():
    return "check errorMessage.txt to see the problem"

def zeroDivMsg(e):
    with open(filename, 'w') as file:
        file.write(f"error: {e} " + "\n")

def generalErrorMsg(e):
    with open(filename, 'w') as file:
        file.write(f"error: {e} " + "\n")
    

try:
    n1 = float(input("input your first number: "))
    n2 = float(input("input your second number: "))
    while True:
        calculatorMenu()
        choice = input("input your choice: ")
        
        if choice == '6':
            print("exiting the calculator")
            break
           
        if choice == '1':
            print("Result: ",add(n1,n2))
        elif choice == '2':
            print("Result: ",substraction(n1,n2))
        elif choice == '3':
            print("Result: ",multiply(n1,n2))
        elif choice == '4':
            print("Result: ",divide(n1,n2))
        elif choice == '5':
            print("Result: ",square(n1,n2) )
        else:
            print("invalid choice")
except ValueError:
    valueErrorMsg()
    checkMsg()
except ZeroDivisionError as e:
    zeroDivMsg(e)
    checkMsg()
except Exception as e:
    generalErrorMsg(e)
    checkMsg()
            