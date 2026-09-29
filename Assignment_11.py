# Assignment No. 11
# Pandas Series: Random numbers, indexing, filtering and statistics

import pandas as pd
import numpy as np

np.random.seed(44)
s = pd.Series(np.random.randint(1, 101, 10))

print("Series:")
print(s)

# Indexing
print("\nValue at index 2:", s[2])

# Filtering
print("\nValues greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

# OUTPUT:
# Series:
# 0    21
# 1    36
# 2    46
# 3    60
# 4    4
# 5    97
# 6    85
# 7    4
# 8    24
# 9    56
# dtype: int64
#
# Value at index 2: 46
#
# Values greater than 50:
3    60
5    97
6    85
9    56
#
# Mean: 43.3
# Median: 41.0
# Minimum: 4
# Maximum: 97