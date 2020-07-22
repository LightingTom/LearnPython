import numpy


data = numpy.genfromtxt('data2.txt',delimiter=',',dtype='str')
print(data)
# We can take out data using indexes as the array
# and it also support negative index like the original array
# it has two forms as shown below
print(data[2][-1])
print(data[2,-1])
# also support slice
print(data[:2])
# : can also represent all
print(data[:,1])  # get scores for each student
# also can mix use the above two attributes
print(data[:,0:2])
# operation on a numpy array will take place in every element
nparray = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(nparray == 5)
# The bool numpy array can also be used as a index
# The row index is the index where the value in column 2 is 5
# we get the whole row from the index
print(nparray[(nparray[:,1] == 5),:])
# Use astype() can change the type of the data in the array
print(nparray.astype(float))
# min(), max(), sum()
print(nparray.min())
print(nparray.min(axis=0))
print(nparray.sum())
print(nparray.sum(axis=1))
# arange(), two different ways to use it
a = numpy.arange(10)  # 1*n matrix, elements: 0~(n-1)
print(a)
b = numpy.arange(0,30,5) # one row, elements: [start, end), the distance is dis
print(b)
# reshape
print(numpy.reshape(a,(2,5)))
print(a.reshape(2,5))
# zeros(), ones(), the default type is float64
print(numpy.zeros((2,3)))
print(numpy.ones((2,3)).dtype)
# numpy.random, the random numbers are ranged from 0 to 1
print(numpy.random.random((2,2)))
# linspace(start,ebd,n): row=1, elements: [start,end), divided into n pieces
print(numpy.linspace(0,10,3))
A = numpy.array([[1,2],[3,4]])
B = numpy.array([[2,3],[4,5]])
# * is element-wise multiplication, and dot() is the matrix multiplication
print(A*B)
print(A.dot(B))
# ravel(): compress the matrix to 1*n
print(A.ravel())
C = numpy.array([[1,2],[3,4],[5,6]])
# transposition
print(C.T)
# hstack and vstack, remeber the parameter must be a tuple
print(numpy.hstack((A,B)))
print(numpy.vstack((A,B)))
# hsplit and vsplit
D = C.T
# The pieces must have a equal division(份数必须可以整除)
print(numpy.hsplit(D,3))
print(numpy.vsplit(D,2))
print(numpy.hsplit(D,(0,1)))
print(numpy.vsplit(D,(0,1)))
# Copy
# The address is the same:
A = B
print(A)
B[1,1] = 1111
A.shape = (1,4)
print(A)
# The address is different but the address of the data is the same
# That is, the operation to the whole matrix won't affect each other,
# but the operation to the element will affect
E = numpy.array([[1,2],[3,4]])
F = E.view()
print(F)
E.shape = (1,4)
print(F.shape)
E[0,0] = 666
print(F)
# Create a clone for the original object
G = numpy.array([[1,2],[3,4]])
H = G.copy()
print(H)
G.shape = (1,4)
print(H.shape)
G[0,0] = 5678
print(H)
# sort, can choose axis=?
S = numpy.array([[33,6],[9,1]])
S.sort(axis=1)
print(S)
S.sort(axis=0)
print(S)
# tile()
# Take the matrix as an element,
# then make a new matrix with it of size m*n
print(numpy.tile(S,(2,2)))
