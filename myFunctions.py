"""
Here, some of the functions which are not available in math library. I am pretty sure,
we can find them in other libraries like numpy, pandas, etc.
"""

import math as mt


def subList(a, b):
    c = []
    if len(a) == len(b):
        for i in range(0,len(a)):
            c.append(b[int(i)]-a[int(i)])
        return c

def dotProd(a, b):
    c = 0
    if len(a) == len(b):
        for i in range(0, len(a)):
            c += a[int(i)]*b[int(i)]
        return c
