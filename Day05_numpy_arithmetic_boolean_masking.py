import numpy as np

# Day 5: NumPy Arithmetic, Comparison and Boolean Masking

# 1. Arithmetic operations
a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 6, 8])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Square:", a ** 2)

# 2. Comparison operations
marks = np.array([35, 45, 60, 75, 90])

print("\nGreater than 50:", marks > 50)
print("Less than 60:", marks < 60)
print("Equal to 75:", marks == 75)

# 3. Boolean masking
passed = marks[marks >= 50]
failed = marks[marks < 50]

print("\nPassed marks:", passed)
print("Failed marks:", failed)