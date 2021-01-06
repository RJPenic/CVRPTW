from instance_loader import *
import os
import sys
from simulated_annealing import sa_algorithm

if __name__ == '__main__':
    instance = str(sys.argv[1])

    cwd = os.getcwd()
    filepath = cwd + '/instances/' + instance

    instance = load_from_file(filepath)
    instance.find_initial_solution()
    print(instance.get_output())
    # instance.generate_random_neighbour()
    # print(instance.get_output())


    # customer = instance.customer_list[46]
    # vehicle = instance.vehicles[24]
    # print(customer)
    # if (vehicle.try_to_serve_customer(customer, 24)):
    #     print(instance.get_output())

    # for i in range(35, 56):
	   #  customer = instance.customer_list[i]
	   #  vehicle = instance.vehicles[24]
	   #  print(customer)
	   #  if (vehicle.try_to_serve_customer(customer, 24)):
	   #  	print(instance.get_output())
	    	# break
    # print(instance)
    sa_algorithm(instance)
