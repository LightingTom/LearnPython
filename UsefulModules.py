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

# struct
# used to transform bytes to other data type
import struct

# for pack(), '>' means it is big-endian mode, 'I' means unsigned 4-byte integer,
# 'H' means unsigned 2-byte integer
# and then, the data needed to be transformed(must follow the type before)
print(struct.pack('>IH', 10240099, 12345))

# provide 2 algorithms: MD5 and SHA1
import hashlib

# The usage of SHA1 is the same(hashlib.sha1()), we don't show here
md5 = hashlib.md5()
# can update many time, the result is all of the content
# To prevent the hacker to get password by comparing the md5 code in the
# database with the md5 code of usually-used passwords, we can store the processed
# md5 code, for example, the password '123456', we can store the md5 code of '123456The-Salt'
# in the database
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# The following code provide a safe way to login
import hashlib, random


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(user, password):
    user = db[user]
    return user.password == get_md5(password + user.salt)


print(login('michael','123456'),',',login('michael','12345678'))

from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))