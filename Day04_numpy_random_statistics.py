import numpy as np

# 1. Random decimal numbers
random_numbers = np.random.rand(5)
print("Random decimals:", random_numbers)

# 2. Random 2D array
random_matrix = np.random.rand(2, 3)
print("Random matrix:")
print(random_matrix)

# 3. Random integers
integers = np.random.randint(1, 100, size=5)
print("Random integers:", integers)