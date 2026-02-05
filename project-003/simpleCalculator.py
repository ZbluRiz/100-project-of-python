#simple calculator 
while True:
    command = input("type 'done' to exit or Press enter to continue: ")
    if command == "done":
        print("calculator closed")
        break
    
    num1 = float(input("input your first number : "))
    num2 = float(input("unput your second number : "))
    operation = input("choose ur arithmetic operation(+,-,/,*) : ")

    #arithmetic operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    else:
        print("wrong input")
        continue
    print(f"Result: {num1} {operation} {num2} = {result}")

