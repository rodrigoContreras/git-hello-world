import datetime

now = datetime.datetime.now()
print(now)

print("++++++++++++++++++++++#")
print(now.year)
print(now.day)
print(now.hour)

dt = datetime.datetime(2020, 5, 21)
print(dt)

print("++++++++++++++++++++++++")
today = datetime.datetime.now()
print(today.strftime('%A'))

day_next_year = today.replace(year=today.year + 1)
print(day_next_year.strftime('%A'))