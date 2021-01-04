from instance_loader import *
import os
import sys

if __name__ == '__main__':
    instance = str(sys.argv[1])

    cwd = os.getcwd()
    filepath = cwd + '/instances/' + instance

    instance = load_from_file(filepath)
    instance.find_initial_solution()
    print(instance.get_output())
    # print(instance)