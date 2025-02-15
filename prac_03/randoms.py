"""
Import random
Print random integer in range [5, 20]
Print random integer from sequence starting at 3, incrementing by 2, stopping before 10
Print random floating-point number in range [2.5, 5.5]
Print random integer in range [0, 100]
"""
import random

print(random.randint(5, 20))  # line 1 smallest:5 largest:18
print(random.randrange(3, 10, 2))  # line 2 smallest:4 largest:7. Couldn't see 4
print(random.uniform(2.5, 5.5))  # line 3 smallest:2.75 largest:5.4
print(random.randint(0, 100))