import keyboard
import time
from datetime import datetime
import os


def period(name:str, start_hour:int, start_minute:int, end_hour:int, end_minute:int):
    global Hour, Minute, Second, Millisecond
    Hour = int(Hour)
    Minute = int(Minute)
    Second = int(Second)
    Millisecond = int(Millisecond)


    #logic to check if the time is before the period
    if start_hour > Hour:
        print(name, ">>  waiting")
    elif start_hour == Hour:
        if start_minute > Minute:
            print(name, ">>  waiting")

    #Logic to check if the time is after the period
    elif end_hour < Hour:
        print(name, ">>  Done")
    elif end_hour == Hour:
        if end_minute < Minute:
            print(name, ">>  Done")


    elif (start_hour <= Hour) or (end_hour >= Hour):
        if (start_minute <= Minute) or (end_minute >= Minute):
            print("In progress....")

    else: #even the else statement won't run and I don't understand why
        print("Error")
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
        '''
        period("Advisroy      ", 8, 30, 8, 50)
        period("Post Ap CS    ", 8, 30, 8, 50)
        period("Econ          ", 8, 30, 8, 50)
        period("AB Calc       ", 8, 30, 8, 50)
        period("Lunch         ", 8, 30, 8, 50)
        period("Study Hall    ", 8, 30, 8, 50)
        period("English       ", 8, 30, 8, 50)
        period("History       ", 8, 30, 8, 50)
        period("PE/Study Hall ", 8, 30, 8, 50)
        '''

        period("asdf          ", 15, 00, 16, 00)
        period("On Time       ", 16, 00, 17, 00) #This won't run or print
        period("Waiting       ", 17, 00, 18, 00)


        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
    print("Task Ended")
