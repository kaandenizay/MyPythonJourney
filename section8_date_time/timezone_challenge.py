from datetime import datetime, timezone

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

# Timezone keys for creating the ZoneInfo objects.
zones = (
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi',
)


# utc_now = datetime.now(tz=timezone.utc) # Get the current time, in UTC
local_now = datetime.now()
# local_now = local_now.replace(microsecond=0)
print(local_now)

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    # required_time = utc_now.astimezone(tz)
    # required_time = datetime.now(tz=tz)
    required_time = local_now.astimezone(tz)
    # The city is the last item, after splitting the zone at the /
    city = zone.split('/')[-1]
    print(f'The time in {city} is {required_time} {required_time.tzname()}')
    # print(f'The time in {city} is {required_time.strftime("%m/%d/%Y %H:%M:%S %z %Z")}')
