# Differnet ways to create array

# 1

a = np.array([1,2,3,4,5], dtype=None)
a.dtype
b = np.array([1,2,3,4,5], dtype=str)
b.dtype

# 2 Zeros

c = np.zeros((2,5), dtype=str)
# (2) this defines only number of zeros in array like simple 1 line list 1D
# (2,3) This defines first number as row and second number as column value so is creates 2D array like 2 rows and three coulmmn
# we can also change Datatype of it using dtype parameter which is written after those values using dtype keyword
# dtype=str → Changes the datatype of each element to string.
# So instead of 0.0, it fills empty strings '' in all places.
c.dtype


# 2 ones

d = np.ones((3,2,4), dtype=int)
# (2) same like zeros it filles with 1 for 4 times but it is 1d array
# (2,4) it create 2 rows and 4 columns filled with 1 this is 2d array
# using  dtype we can set datatype of that ones array
d.dtype


# 3 full

e = np.full((2,3), 5, dtype=str)
# (2,3) = This defines a 2D array with 2 rows and 3 columns
# The second argument '5' means fill all elements with the value 5
# dtype=int = This sets the datatype of all elements as integer
# So it creates a 2D array where every cell has number 5 in integer form
e

# 6 arange() array with step size like range

f = np.arange(1, 11, 2, dtype=int)
# np.arange(start, stop, step) = generates numbers from start to stop (excluding stop) with step size
# (1, 11, 2) = starts from 1, goes up to 11 (not including 11), and increases by 2 each time
# So it will generate: 1, 3, 5, 7, 9
# dtype=int = sets the datatype of all elements as integer
# So it creates a 1D array of odd numbers from 1 to 10
# step size goes like this = 0.1 , 0.2
f.dtype

# 7 linspace() linearly spaced values

g = np.linspace(1,11,num=3,endpoint=False,dtype=int)
# (1, 11) = defines start and end range of values
# num=12 = total 12 values will be created between 1 and 11
# endpoint=True = include 11 in the array
# dtype=int = convert float results to integer
# Since values are evenly spaced as float, then converted to int, some values may repeat


# 8 eye() indentity matrix 

f = np.eye(3, 2,dtype=float)
# np.eye(rows, columns) = creates a 2D array with 1s on diagonal and 0s elsewhere
# (3, 2) = 3 rows and 2 columns
# So it creates a 2D matrix with diagonal 1s from top-left
# If rows > columns, extra rows will have all 0s at the bottom
f.dtype


# 9 random.rand() default use 0 and 1 to create ramdom matrix 

g = np.random.rand(2, 3)
# np.random.rand(rows, columns) = creates 2D array with random float values between 0.0 and 1.0
# (2, 3) = means 2 rows and 3 columns
# Each value is different every time you run
g.dtype

h = np.random.randint(1, 10, size=(2, 3))
# np.random.randint(start, stop, size=(rows, columns)) → creates 2D array with random integers
# (1, 10) = numbers from 1 to 9 (10 is not included)
# size=(2, 3) = means 2 rows and 3 columns
# Each value will be random integer between 1 to 9
h.dtype
