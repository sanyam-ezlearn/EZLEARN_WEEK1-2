'''Construct the Rectangle'''
import math
def constructRectangle(area):
    w = int(math.sqrt(area))
    while area % w != 0:
        w -= 1
    return [area // w, w]

area = 24
print(constructRectangle(area))