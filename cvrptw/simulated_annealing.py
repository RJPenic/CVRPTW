import instance_loader
import random

def sa_algorithm(instance, temp_start = 100, update_temp = lambda t, i : 0.999 * t, stop_criterion = lambda t : t <= 1e-4):
    curr_solution = incumb_solution = instance.copy().find_initial_solution()
    curr_dist, curr_vhcls = incumb_dist, incumb_vhcls = curr_solution.get_total_distance_and_vehicles()

    temp = temp_start

    while not stop_criterion(temp):
        neighbour = curr_solution.copy()
        neighbour.generate_random_neighbour()

        neighbour_dist, neighbour_vhcls = neighbour.get_total_distance_and_vehicles()

        if (neighbour_vhcls < curr_vhcls or neighbour_dist < curr_dist) or random.random() < exp(- (curr_dist - neighbour_dist) / temp):
        	curr_solution = neighbour
        	curr_dist, curr_vhcls = neighbour_dist, neighbour_vhcls

        	if (curr_vhcls < incumb_vhcls or curr_dist < incumb_dist):
        		incumb_solution = curr_solution
        		incumb_dist, incumb_vhcls = curr_dist, curr_vhcls


        temp = update_temp(temp)

    return incumb_solution


