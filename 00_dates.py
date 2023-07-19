## Dates ##

# Importing the datetime module

from datetime import datetime

from datetime import time

from datetime import date

import datetime

# Creating a date object

d = datetime.date(2019, 4, 13)

print(d)

# Printing the current date

tday = datetime.date.today()

print(tday)

hour_2 = datetime.datetime.now().hour

hour = datetime.datetime.now()

print(hour)

#while True:
#    print(datetime.datetime.now())
#    
#    if datetime.datetime.now().hour == 22:
#        break

time_stap = datetime.datetime.timestamp(hour)

print(time_stap)

year2023 = datetime.date(2023, 1, 1)

def print_date(date):
    
    print(date)

print_date(hour_2)    

print("#--------------------------------------#")

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


print("#--------------------------------------#")

# Creating a datetime object

dt = datetime.datetime(2019, 4, 13, 21, 6, 0)

print(dt.fromisocalendar(2019, 15, 6))

print(dt.fromisoformat('2019-04-13 21:06:00'))


print("#--------------------------------------#")

current_date = date(2002, 10, 6)

print(current_date.year)

print(current_date.month)

print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

diff = current_date - date.today()

print(diff)


print("#--------------------------------------#")

from datetime import timedelta

# Creating a timedelta object

#el timedelta sirve para calculcar franjas de dias mas no para sumar fechas

time_delta = timedelta(200, 100, 100, weeks= 10)

end_delta = timedelta(300, 100, 100, weeks= 13)

print(time_delta + end_delta) #se puede hacer todas las operaciones matematicas


