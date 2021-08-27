"""
    array
        Example 2.20

    collections.deque
        Example 2.23
"""

# Example 2.20
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

# Example 2.21
from array import array
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
print(numbers)

# Example 2.23
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
#
dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)