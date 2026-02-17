import random, string

def generatePassword(length = 12):
    filename = 'project-014/passwordSaver.txt'
    if length < 4:
        raise ValueError('password length must be at least 4 characters')
    
    #password character sets
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    #ensure at least one of each character type
    password1 = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
    password2 = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
    password3 = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
    password4 = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
    
    
    #fill the remaining length
    choice = input("do you want to add special chars (yes/no): ").lower()
    while True:
        if choice == 'yes':
            all_chars = uppercase + lowercase + digits + special_chars
            break
        elif choice == 'no':
            all_chars = uppercase + lowercase + digits
            break
        else:
            print("please input the right choice")
        
    #sum all of the password into 1 variable    
    password1 += random.choices(all_chars,k =length - 4)
    password2 += random.choices(all_chars,k =length - 4)
    password3 += random.choices(all_chars,k =length - 4)
    password4 += random.choices(all_chars,k =length - 4)
    
    #shuffle the password
    random.shuffle(password1)
    random.shuffle(password2)
    random.shuffle(password3)
    random.shuffle(password4)
    
    #join to show the password as a string
    final1 = "".join(password1)
    final2 = "".join(password2)
    final3 = "".join(password3)
    final4 = "".join(password4)
    
    #show the list of password
    print("\n-Password List-")
    print(f"first password: {final1}")
    print(f"second password: {final2}")
    print(f"third password: {final3}")
    print(f"fourth password: {final4}")
    
    password_chooser = input("\nwhich password do you want to save(1/2/3/4): ")
    while True:
        if password_chooser == '1':
            password = password1
            break
        elif password_chooser == '2':
            password = password2
            break
        elif password_chooser == '3':
            password = password3
            break
        elif password_chooser == '4':
            password = password4
            break
        else:
            print("please choose the right choice")
    
    #save to notepad  
    with open(filename,'w') as file:
        file.write("".join(password)),
    
    return ''.join(password)
    
        
try:
    length = int(input("enter the desire password length(minimum 4): "))
    password = generatePassword(length)
    print("Generated Password: ",password)
except ValueError as e:
    print(e)
    