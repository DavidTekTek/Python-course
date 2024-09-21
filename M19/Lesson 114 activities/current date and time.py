from datetime import date, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\n Current Date and Time is", now)

print("\n Date components", today.year, today.month, today.day)