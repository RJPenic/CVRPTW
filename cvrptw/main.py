from instance_loader import *
import os
import sys
from simulated_annealing import sa_algorithm

if __name__ == '__main__':
    instanceName = str(sys.argv[1])

    cwd = os.getcwd()
    filepath = cwd + '/instances/' + instanceName

    instance = load_from_file(filepath)
    instance.find_initial_solution()
    instance.get_output()

    results = sa_algorithm(instance)

    with open("1min_" + instanceName, "w") as f:
    	f.write(results[0].get_output())

    with open("5min_" + instanceName, "w") as f:
    	f.write(results[1].get_output())

    with open("infinite_" + instanceName, "w") as f:
    	f.write(results[2].get_output())
