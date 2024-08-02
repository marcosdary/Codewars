from datetime import datetime
from dateutil.relativedelta import relativedelta

def count_days(d):
    now = datetime.now()
    if d.date() == now.date():
        return "Today is the day!"
    if now > d:
        return "The day is in the past!"
    r = d - now
    
    print(d)
    return f"{r} days"
# 2040-01-24 18:43:00
d = datetime(2040,1,24, 18,43,0)
print(count_days(d))