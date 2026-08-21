import numpy as np
# numpy is basically for fast calculation ,its a c program wrapped in python 
# NumPy = Numerical Python
# It is used for:Fast calculations,Arrays (better than Python lists),Data science & ML foundation

# a=np.array([1,2,3])
# print(a)

# # 2d and 3d array
# b=np.array([[1,2,3],[4,5,6]])
# print(b)

# # dtype
# d=np.array([1,2,3],dtype=float)
# print(d)

# # arange
# r=np.arange(1,11,2)
# print(r)

# # with reshape 
# re=np.arange(16).reshape(2,2,2,2)
# print(re)

# # np.ones and np.zeros
# print(np.ones((3,4)))
# print(np.zeros((3,4)))

# # np.random
# print(np.random.random((3,4))) #from random class select random method

# # np.linspace : start to end create array with number of equal spacing
# print(np.linspace(-10,10,10,dtype=int)) #total 10 elements including -10 and 10

# # np.identity
# print(np.identity(3))


# --------------------------------------Array Attributes----------------------------------------------------------------------------------------

a1=np.arange(10,dtype=np.int32)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
# print(a1)
# print(a2)
# print(a3)

# # ndim : tells the dimension
# print(a3.ndim)
# print(a3.shape)

# /size
print(a2.size)

#itemsize  : int 32 takes 4 bytes whereas int 64 takes 8 bytes
print(a3.itemsize)  # int 64 is default
print(a1.itemsize)

# dtype : to know datatype 
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# changing datatype 
# astype
print(a3.astype(np.int32)) #we changed the default int64 as int32

