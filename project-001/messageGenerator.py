from datetime import datetime
#welcome message generator

username = input("input your username: ")
hobby = input("input your hobby: ").lower()
color = input("what's your favorite color: ")
now = datetime.now()

#message personalized

print("\nWelcome Message")
print(f"hello name {username}!")
print(f"your hobby is {hobby}")
print(f"and your favorite color is {color}")
print(f"it's great to know you like {hobby} ")
print(f"happy new year!! {now.year}")