from datetime import datetime
def time_for_milk_and_cookies(dt):
    dt = datetime.strptime(dt, '%Y-%m-%d')
    return dt.month == 12 and dt.day == 24

