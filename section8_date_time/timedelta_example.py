import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

start = datetime.date(2022, 2, 4)
print(start)

duration = datetime.timedelta(days=15)
end = start + duration
print(end)
print(type(end))
print(duration)

duration = datetime.timedelta(days=15, hours=48)
end = start + duration
print(end)
print(duration)

d1 = datetime.timedelta(hours=2)
d2 = datetime.timedelta(minutes=120)
d3 = datetime.timedelta(seconds=7200)

print(d1, d2, d3, sep=', ')
print(repr(d1), repr(d2), repr(d3), sep=', ')

difference = end - start
print(repr(difference))
print(difference == duration)
