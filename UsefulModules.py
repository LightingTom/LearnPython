# Module: datetime
from datetime import datetime, timedelta

now = datetime.now()
print(now)

# 自定时间
dt = datetime(2020, 6, 29, 16, 43)
print(dt)

# datetime to timestamp
print(dt.timestamp())

# timestamp to datetime
print(datetime.fromtimestamp(1593420307.25048))

# convert string to datetime
cday = datetime.strptime('2020-6-1 16:47:50', '%Y-%m-%d %H:%M:%S')
print(cday)

# convert time to string
# %a: mon,tue...
# %A: monday, tuesday...
# %w: 0,1,2...(星期几)
# %b, %B: The name of the month
# %d: 01-31(日期)
# %m: 01-12(月份)
print(now.strftime('%A, %B %d %H:%M'))

# The calculation of datetime
print(now + timedelta(days=2))
print(now - timedelta(hours=3))

# Module collections
# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('The x-axis is', p.x, 'The y-axis is', p.y)


# Counter
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
# Update the count automatically
c.update('hello')
print(c)

