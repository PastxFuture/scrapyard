#Importing all the necessary libraries to form the alarm clock:
import datetime
import time

def alarm(set_alarm_timer):
    
    while True:
        time.sleep(1)

        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(f'The time is {now}')

        if now == set_alarm_timer:
            print("Time to Wake up")
            break


alarm('19:25:35')