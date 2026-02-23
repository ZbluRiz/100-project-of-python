from datetime import datetime,timedelta
import time

#getting the event date

def getEventdate():
    try:
        date_input = input("input your date (YYYY-MM-DD HH-MM-SS): ")
        return datetime.strptime(date_input,"%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("please use YYYY-MM-DD HH-MM-SS")
        return None

#calculate the time
def calculateTime(event_date):
    current_time = datetime.now()
    time_difference = event_date - current_time
    return time_difference

#display countdown
def displayCountdown(time_left):
    days = time_left.days
    hours,remainder = divmod(time_left.seconds,3600)
    minutes,seconds = divmod(remainder, 60)
    print(f"\nTime Remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="")

#main countdown loop
def startCountdown(event_date):
    while True:
        time_left = calculateTime(event_date)
        if time_left.seconds <= 0:
            print("\ncountdown complete!")
            break
        displayCountdown(time_left)
        time.sleep(1)


# Main Program
event_datetime = getEventdate()
if event_datetime:
  print(f"Event set for: {event_datetime}")
  startCountdown(event_datetime)