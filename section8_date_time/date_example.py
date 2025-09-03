import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A %d %B, %Y')
print(pretty_start)

year = start.year
month = start.month
day = start.day

print("The {} winter olympics started on day of {} of month {}".format(
  year, month, day
))

today = datetime.date.today()
print(today)
print(today.strftime('%A'))
print(today.weekday()) # Monday is zero, not 1
