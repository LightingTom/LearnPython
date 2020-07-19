import numpy
import pandas

# data = numpy.genfromtxt('data2.txt',delimiter=',',dtype='str')
# print(data)

# core structure: DataFrame
# data2.head(n), display the first n lines of the data, default is 5
# data2.tail(n), display the last n lines of the data, default is 5
data2 = pandas.read_csv("table.csv")
print(data2.dtypes)
print(data2.shape)
print(data2.tail())

