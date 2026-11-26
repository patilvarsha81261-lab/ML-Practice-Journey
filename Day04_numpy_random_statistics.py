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

# 4. Random 2D integers
matrix = np.random.randint(1, 10, size=(3, 3))
print("Random integer matrix:")
print(matrix)

# 5. Random decimal values using random()
decimal_values = np.random.random(4)
print("Random values:", decimal_values)

# 6. Seed
np.random.seed(42)
seed_numbers = np.random.randint(1, 100, size=5)
print("Seed numbers:", seed_numbers)