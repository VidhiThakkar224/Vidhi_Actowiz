'''The datetime module is used to:

Get current date and time
Format date/time
Perform calculations (like adding days)
Compare dates'''

import datetime
from datetime import timedelta,tzinfo

#current date time

now = datetime.datetime.now()
print(now)

#change date

d = datetime.date(2004, 2, 2)
print(d)

#convert strng to date

date_string = "29-05-2026"
date_obj = datetime.datetime.strptime(date_string, "%d-%m-%Y")

print(date_obj)

#date calculate

today = datetime.date.today()

future = today + datetime.timedelta(days=50)
print(future)

#date differance

d1 = datetime.date(2026, 4, 29)
d2 = datetime.date(2004, 2, 2)

diff = d1 - d2
print(diff.days)

#weekday name in short
print(d.strftime("%a"))
#weekday name in full
print(d.strftime("%A"))

#same for month name
print(d.strftime("%b"))
print(d.strftime("%B"))

