#number comparison program
while True:
    command = input("type 'done' to exit or Press enter to continue: ")
    if command == "done":
        print("program is closed")
        break
    
    num1 = float(input("input your first number: "))
    num2 = float(input("input your second number: "))
    num3 = float(input("input your third number: "))
    
    print("\nNumber Comparison Program")
    if num1 == num2 and num1 == num3 and num2 == num3:
        print("the number are equals")
    elif num1 > num3 and num1 > num2:
        print(f"{num1} is bigger than {num2} or {num3}")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is bigger than {num1} or {num3}")
    elif num3 > num1 and num3 > num1:
        print(f"{num3} is bigger than {num1} or {num2}")
    else:
        print("two number is bigger than others")
        
    if num1 == 0 or num2 == 0 or num3 == 0:
        print("\none or two number is zero")
    else:
        print("\nno zero number")