
import time
import datetime
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
current = datetime.datetime(year, month, day)

print("\nDate and time:", current.strftime("%d-%m-%Y %H:%M:%S"))
print("Year:", current.year)
print("Month of the year:", current.strftime("%B"))
print("Week number of the year:", current.strftime("%U"))
print("Weekday of the week:", current.strftime("%A"))
print("Day of the year:", current.strftime("%j"))
print("Day of the month:", current.day)
print("Day of week:", current.weekday())

