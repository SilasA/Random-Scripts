import sys
import math

def calc_root(a, b, c):
    r = b*b - 4*a*c
    if (r < 0):
        return -1
    return math.sqrt(r)

def calc_formula(a, b, c):
    pass

if (len(sys.argv) != 4):
    print("Invalid Args")
    exit()

solution = [calc_formula(sys.argv[1], sys.argv[2], sys.argv[3])]

