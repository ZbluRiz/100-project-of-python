import time

start = int(input("Enter the number to start the countdown: "))
timing = int(input("input the countdown interval: "))
msg = input("input the message after the countdown end: ")

while start > 0:
    print(start)
    time.sleep(timing)
    start -= 1
    
print(msg)