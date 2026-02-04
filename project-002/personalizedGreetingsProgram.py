#personalized greetings program

#ask for the user data
name = input("what is your name? ")
age = int(input("how old are you? "))
days = input("how was your days?good/bad? ")
color = input("what's your favorite color? ")

print("hello nice to meet you {}!".format(name))
print(f"You are {age} and {color} is very beautiful color")
if days == "good":
    print("glad to hear that")
else:
    print("sorry to hear that, hope your days getting better")
