import datetime

today = datetime.datetime.now()
# 17:27:30

d = datetime.datetime(today.year, today.month, today.day, 12, 15, 29)
def minutes_to_midnight(d:datetime.datetime) -> str:
    midnight = 24 * 60
    d_minute =  d.hour*60 + d.minute + d.second / 60
    return f'{midnight - d_minute:.0f} minutes'   
print(minutes_to_midnight(d)) # "37 minutes"

