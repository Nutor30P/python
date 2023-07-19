## Modules ###

import datetime

print(datetime.date.today())

from datetime import date

print(date.today())

from datetime import date as d

print(d.today())

from datetime import date, timedelta

print(date.today() + timedelta(days=2))

from modules import sum

sum(1, 2)


from statistics import *

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(mean(agesData))

print(median(agesData))

print(mode(agesData))

print(stdev(agesData))