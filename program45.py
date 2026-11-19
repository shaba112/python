
import datetime
import time

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
 
today = datetime.date(year, month, day)

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

