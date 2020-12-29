from math import sqrt

def distance(customer1, customer2):
    diff_x = customer1.x - customer2.x
    diff_y = customer1.y - customer2.y
    return sqrt(diff_x * diff_x + diff_y * diff_y)

