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
    print()
    print(f'Instance initial solution: {instanceName}')
    instance.get_output()

    results = sa_algorithm(instance)

    print()
    print(f'Instance {instanceName} after 1 min')
    with open("res-1m-" + instanceName, "w") as f:
    	f.write(results[0][0].get_output())
    print("Objective function count: ", results[0][1])

    print()
    print(f'Instance {instanceName} after 5 min')
    with open("res-5m-" + instanceName, "w") as f:
    	f.write(results[1].get_output())
    print("Objective function count: ", results[1][1])

    print()
    print(f'Instance {instanceName} in the end')
    with open("res-un-" + instanceName, "w") as f:
    	f.write(results[2].get_output())
    print("Objective function count: ", results[2][1])
