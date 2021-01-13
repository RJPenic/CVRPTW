import instance_loader
import random
from copy import deepcopy
from math import exp
import time

def sa_algorithm(instance, temp_start = 100, update_temp = lambda t : 0.999 * t, stop_criterion = lambda t : t <= 0.01):
    curr_solution = incumb_solution = deepcopy(instance)
    # print("Inside sa: ", instance.get_total_distance_and_vehicles())
    curr_dist, curr_vhcls = incumb_dist, incumb_vhcls = curr_solution.get_total_distance_and_vehicles()

    temp = temp_start

    start = time.time()
    afterOneMin = None
    afterFiveMin = None
    total = None

    while not stop_criterion(temp):
        print(temp, incumb_vhcls, incumb_dist)
        neighbour = deepcopy(curr_solution)
        neighbour.generate_random_neighbour()

        neighbour_dist, neighbour_vhcls = neighbour.get_total_distance_and_vehicles()

        if (neighbour_vhcls < curr_vhcls or neighbour_dist < curr_dist) \
            or random.random() < exp(- (abs(curr_dist - neighbour_dist)) / temp):
        	curr_solution = neighbour
        	curr_dist, curr_vhcls = neighbour_dist, neighbour_vhcls

        	if (curr_vhcls < incumb_vhcls or curr_dist < incumb_dist):
        		incumb_solution = curr_solution
        		incumb_dist, incumb_vhcls = curr_dist, curr_vhcls


        temp = update_temp(temp)
        if not afterOneMin and time.time() - start >= 60:
            afterOneMin = deepcopy(incumb_solution)
        if not afterFiveMin and time.time() - start >= 5 * 60:
            afterFiveMin = deepcopy(incumb_solution)

    if not afterOneMin:
        afterOneMin = incumb_solution
    if not afterFiveMin:
        afterFiveMin = incumb_solution

    print(time.time() - start)
    return [afterOneMin, afterFiveMin, incumb_solution]


