import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
  cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
  tzfmt = r'UTC([+-][0-9]+):([0-9]+)'
  tz_group=re.match(tzfmt, tz_str).groups()
  if tz_group:
    tz = int(tz_group[0])+int(tz_group[1])/60
    cday = cday.replace(tzinfo=timezone(timedelta(hours=tz)))
    return cday.timestamp()
  else:
    return None

 
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')