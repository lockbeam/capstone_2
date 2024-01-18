from datetime import datetime, date, time

today = date.today()
print(today)

#year monnth day is a standard format
tomorrow = date(2023, 1, 17)
print(tomorrow)

next_week = date.fromisoformat('2020-01-22')
print(next_week)

#get a timestamp
right_now = datetime.now()
print(right_now)

#number of seconds since 01/01/1970
print(right_now.timestamp)

# asign a date using seconds from 01/01/1970
# in this case this would be 2017-07-13 at 21:40:00
my_date = datetime.fromtimestamp(150000000)
print(my_date)
