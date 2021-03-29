# Draw a square
# All points are sqrt(x^2+y^2) away from the orgin
# If that value is > 1 it is inside the circle
# pi*r^2 / (2* r)^2 = (4 *number of points inside the circle) / num outside the circle
# Solve for pi
import random

def calculatePi(n):
    inside = 0.0
    total = 0.0
    for _ in range(n):
        randX = random.uniform(0,1)
        randY = random.uniform(0,1)
        distance = randX**2 + randY**2
        if distance <= 1:
            inside = inside + 1.0
        total = total + 1.0
    pi = (4.0*inside)/total
    return pi
print(calculatePi(1000))
