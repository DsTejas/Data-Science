import numpy as np

# l: Reverse a 1D array
l = np.array([1, 2, 3, 4, 5])
l = l[::-1]  # reverse the array
print("l =", l)  # [5 4 3 2 1]

# m: Reverse columns of 2D array
m = np.array([[1, 2, 3], [4, 5, 6]])
m = m[:, ::-1]  # reverse each row (columns)
print("m =\n", m)
# [[3 2 1]
#  [6 5 4]]

# n: Filter values using condition
n = np.array([10, 15, 20, 25])
n_filtered = n[n >= 20]  # only values >= 20
print("n =", n_filtered)  # [20 25]

# o: Multiply all elements
o = np.array([2, 4, 6])
o = o * 10  # multiply every value by 10
print("o =", o)  # [20 40 60]

# p: Broadcast value to entire array
p = np.ones((2, 3), dtype=int)
p += 5  # add 5 to all elements
print("p =\n", p)
# [[6 6 6]
#  [6 6 6]]

# q: Matrix multiplication
q1 = np.array([[1, 2], [3, 4]])
q2 = np.array([[5, 6], [7, 8]])
q = np.dot(q1, q2)  # matrix multiplication
print("q =\n", q)
# [[19 22]
#  [43 50]]

# r: Transpose of 2D array
r = np.array([[1, 2, 3], [4, 5, 6]])
r = r.T  # transpose → rows become columns
print("r =\n", r)
# [[1 4]
#  [2 5]
#  [3 6]]

# s: Clip values in array (limit min and max)
s = np.array([5, 15, 25, 35])
s = np.clip(s, 10, 30)
# values below 10 become 10, above 30 become 30
print("s =", s)  # [10 15 25 30]

# t: Replace NaN values with 0
t = np.array([1, np.nan, 3, np.nan, 5])
t = np.nan_to_num(t, nan=0)
# replaces all np.nan with 0
print("t =", t)  # [1. 0. 3. 0. 5.]
