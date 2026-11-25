import numpy as np

# 1. Zeros
arr1 = np.zeros(5)
print("Zeros:", arr1)

# 2. Ones
arr2 = np.ones(5)
print("Ones:", arr2)


# 3. Arange
arr3 = np.arange(1, 11)
print("Arange:", arr3)

# 4. Arange with step
arr4 = np.arange(2, 11, 2)
print("Even numbers:", arr4)

# 5. Linspace
arr5 = np.linspace(1, 10, 5)
print("Linspace:", arr5)

# 6. Full
arr6 = np.full(5, 7)
print("Full:", arr6)

# 7. Data type
arr7 = np.array([1, 2, 3, 4], dtype=float)
print("Float array:", arr7)
print("Data type:", arr7.dtype)

