from datetime import time
def can_i_play(now_hour, start_hour, end_hour):
    now_hour = time(hour=now_hour)
    start_hour = time(hour=start_hour)
    end_hour = time(hour=end_hour+24)
    return start_hour < now_hour < end_hour

print(can_i_play(23, 22, 1))