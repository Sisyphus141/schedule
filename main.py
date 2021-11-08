##Version 0.0.1


import keyboard
import time
from datetime import datetime
import os
Hour = 0
Minute = 0
Second = 0
Millisecond = 0



def period(name:str, start_hour:int, start_minute:int, end_hour:int, end_minute:int):
    '''
    if Hour != end_hour time_left +
    '''


    time_left = int(end_minute) - int(Minute)

    #logic to check if the time is before the period
    if int(start_hour) > int(Hour):
        print(name, ">>  waiting")
    elif int(start_hour) == int(Hour):
        if int(start_minute) > int(Minute):
            print(name, ">>  waiting")

    #Logic to check if the time is after the period
    elif int(end_hour) < int(Hour):
        print(name, ">>  Done")
    elif end_hour == Hour:
        if int(end_minute) < int(Minute):
            print(name, ">>  Done")

    else: #even the else statement won't run and I don't understand why
        print(name, ">>  In Pogress >> Time Left:", time_left)
try:
    while True:
        Time = str(datetime.now())
        #Split date and time
        Date, Time = Time.split(" ")
        #Splits off millisecond by "."
        Time, Millisecond = Time.split(".")
        #Splits time into hour, minut, second by ":"
        Hour, Minute, Second = Time.split(":")

        #class(name, start_hour, start_minute, end_hour, end_minute)
        period("Advisroy      ", 8, 30, 8, 50)
        period("Post Ap CS    ", 8, 50, 9, 50)
        period("Econ          ", 9, 55, 10, 50)
        period("AB Calc       ", 10, 55, 11, 50)
        period("Lunch         ", 8, 30, 8, 50)
        period("Study Hall    ", 8, 30, 8, 50)
        period("English       ", 12, 50, 13, 45)
        period("History       ", 13, 50, 14, 45)
        period("PE/Study Hall ", 14, 50, 15, 45)



        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
    print("Task Ended")
