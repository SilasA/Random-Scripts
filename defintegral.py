# A simple script to find an estimate for the area under the curve
# f(x) on interval [x, y] with n number of rectangles with
# p end point

import sys

x = 0
y = 0
n = 0

def f(x):
    return -1 # function here

def calc(x, y, n, p):
    rectWidth = (y - x) / n
    itr = rectWidth * p + x
    areaAccum = 0.0
    for i in range(n):
        areaAccum += rectWidth * f(itr)
        itr += rectWidth
    return areaAccum

x = float(input("Lower Bound: "))
y = float(input("Upper Bound: "))
n = int(input("Number of Rectangles: "))

print("Left endpoint")
print(calc(x, y, n, 0))

print("Middle endpoint")
print(calc(x, y, n, 0.5))

print("Right endpoint")
print(calc(x, y, n, 1))
