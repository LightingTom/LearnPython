# 导入socket库:
import socket

# 创建一个socket:
# IPv4协议，IPv6为AF_INET6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
# connect的参数为一个tuple, 分别为服务器地址和端口号
s.connect(('https://www.liaoxuefeng.com/', 80))
s.send(b'GET / HTTP/1.1\r\nHost: https://www.liaoxuefeng.com/\r\nConnection: close\r\n\r\n')
# 接收数据:
# 使用recv()方法，一次最多接受1k数据
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭链接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
