import random, string

def generatePassword(length = 12):
    if length < 4:
        raise ValueError('password length must be at least 4 characters')
    
    #password character sets
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    #ensure at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
    
    #fill the remaining length
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars,k =length - 4)
    
    #shuffle the password
    random.shuffle(password)
    
    return ''.join(password)

try:
    length = int(input("enter the desire password length(minimum 4): "))
    password = generatePassword(length)
    print("Generated Password: ",password)
except ValueError as e:
    print(e)
    