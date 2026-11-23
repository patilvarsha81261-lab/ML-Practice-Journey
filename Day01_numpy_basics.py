#Import NumPy
import numpy as np
print("NumPy version:", np.__version__)


#A. Create an array
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a)

#B. Add numbers

import numpy as np

a = np.array([10, 20, 30])

print(a + 5)


#C. Multiply array elements
import numpy as np

a = np.array([2, 4, 6])

print(a * 3)

#D. Calculate the mean (average)

import numpy as np

marks = np.array([70, 80, 90, 60, 100])

print(np.mean(marks))

#E. Find maximum and minimum

import numpy as np

numbers = np.array([23, 45, 12, 67, 89])

print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))