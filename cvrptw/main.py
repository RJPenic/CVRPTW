from instance_loader import *
import os
import sys
from simulated_annealing import sa_algorithm

if __name__ == '__main__':
    instance_file = str(sys.argv[1])
    instance = load_from_file(instance_file)
    sa_algorithm(instance)