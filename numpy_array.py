import numpy as np

# Creating a 1D array
arr1 = np.array([10, 20, 30])
print("1D array:", arr1)

# Access and update a value in 1D
print("First element:", arr1[0])
arr1[0] = 99
print("Updated 1D array:", arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:", arr2)

# Access and update a value in 2D
print("Element in second row, third column:", arr2[1][2])
arr2[1][2] = 100
print("Updated 2D array:", arr2)

# Creating a 3D array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("3D array:", arr3)

# Access and update a value in 3D
print("Element at position [1][0][1]:", arr3[1][0][1])
arr3[1][0][1] = 55
print("Updated 3D array:", arr3)
