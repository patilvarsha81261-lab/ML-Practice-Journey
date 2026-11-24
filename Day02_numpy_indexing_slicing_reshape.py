import numpy as np

# 1. Indexing
arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Last element:", arr[-1])

# 2. Slicing
print("First three:", arr[:3])
print("Middle elements:", arr[1:4])
print("Reverse:", arr[::-1])


# 3. 2D Array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Element:", matrix[1, 2])
print("Second row:", matrix[1])
print("Second column:", matrix[:, 1])



# 4. Reshape
numbers = np.array([1, 2, 3, 4, 5, 6])

reshaped = numbers.reshape(3, 2)
print("Reshaped array:")
print(reshaped)

# 5. Shape
print("Shape:", reshaped.shape)