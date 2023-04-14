a = [20,10,30,40]
print(a)
print(id(a))
a.sort()
print(a)
print(id(a))

import random

random.shuffle(a)
print(a)
print(id(a))
