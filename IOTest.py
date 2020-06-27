# The same format with C

try:
    infile = open('D://pytest//1.txt','r')
    print(infile.read())
finally:
    if infile:
        infile.close()


# The above code equals to the following
# It can also specify encoding: open('path', 'r', encoding = 'gbk')
with open('D://pytest//1.txt','r') as infile:
    print(infile.read())

# Output file is also the same
with open('D://pytest//3.txt','w',encoding='gbk') as out:
    out.write('中国\n')

with open('D://pytest//3.txt','r',encoding='gbk') as inp:
    print(inp.read())