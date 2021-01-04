from util import *
from math import ceil
import random


class Customer:
    def __init__(self, cust_no, x, y, demand, ready_time, due_date, service_time):
        self.cust_no = cust_no
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_time = service_time
        self.is_served = False

    def served(self, vehicle_num):
        self.is_served = True
        self.vehicle_num = vehicle_num

    def __str__(self):
        return f'Customer NO. : {self.cust_no}; X : {self.x}; Y : {self.y}; Demand : {self.demand}; Ready Time : {self.ready_time}; Due Date : {self.due_date}; Service Time : {self.service_time}'

class Vehicle:
    def __init__(self, depo, max_capacity, min_capacity=0):
        self.x = depo.x
        self.y = depo.y
        self.max_capacity = max_capacity  
        self.min_capacity = min_capacity
        self.capacity = max_capacity
        self.last_service_time = 0
        self.service_route = [(depo, 0)]
        self.total_distance = 0
        self.depo = depo

    def serve_customer(self, customer, vehicle_num):
        if not (customer.ready_time <= (ceil(distance(customer, self)) + self.last_service_time) <= customer.due_date) or self.capacity <= customer.demand:
            return False
        if self.depo.due_date < ceil(distance(customer, self)) + self.last_service_time + customer.service_time + distance(customer, self.depo):
            return False
        dist = distance(customer, self)
        self.x = customer.x
        self.y = customer.y
        self.capacity -= customer.demand
        self.last_service_time += ceil(dist)
        self.service_route += [(customer, self.last_service_time)]
        self.last_service_time += customer.service_time
        customer.served(vehicle_num)
        self.total_distance += dist
        if self.capacity < self.min_capacity:
            self.return_home()
        return True

    def serve_customer_force(self, customer, vehicle_num):
        if customer.ready_time > ceil(distance(customer, self)) + self.last_service_time:
            last_service_time = self.last_service_time
            self.last_service_time += customer.ready_time - ceil(distance(customer, self)) + self.last_service_time
            if self.serve_customer(customer, vehicle_num):
                return True
            else:
                self.last_service_time = last_service_time
        return False

    def return_home(self):
        if self.x != self.depo.x or self.y != self.depo.y:
            self.capacity = self.max_capacity
            self.last_service_time += ceil(distance(self, self.depo))
            self.service_route += [(self.depo, self.last_service_time)]
            self.x = self.depo.x
            self.y = self.depo.y

    # TODO remove customer from list of served ones and update the rest
    def remove_customer(self, customer):
        # --->
        self.reset_vehicle_used()

    # TODO try out every combination for this vehicle and save it if its valid
    def try_to_serve_customer(self, customer, vehicle_num):
        # --->
        return

    def reset_vehicle_used(self):
        if self.service_route[0] == self.service_route[1]:
            self.service_route = self.service_route[:1]
            self.last_service_time = 0
            self.capacity = self.max_capacity
            self.total_distance


class Instance:
    def __init__(self, num_vehicles, capacity, customer_list):
        assert (
            num_vehicles > 0 and capacity > 0
        ), f'Number of vehicles and their capacity must be positive! {num_vehicles}, {capacity}'
        self.num_vehicles = num_vehicles
        self.capacity = capacity
        self.vehicles_used = 0

        customer_list.sort(key=lambda c: c.ready_time)
        depo = customer_list[0]
        self.vehicles = [Vehicle(depo, capacity) for _ in range(num_vehicles)]
        assert (
            customer_list[0].cust_no == 0 and customer_list[0].ready_time == 0 and customer_list[0].demand == 0
        ), f'Customer list must contain depot with customer number 0!'
        self.customer_list = customer_list

    def __getitem__(self, key):
        return self.customer_list[key]

    def __str__(self):
        result = f'Vehicle Number: {self.num_vehicles}; Capacity: {self.capacity};'
        for customer in self.customer_list:
            result += f'\n{customer}'
        return result

    def sort_by_ready_time(self):
        self.customer_list.sort(key=lambda c: c.ready_time)

    def find_initial_solution(self):
        for customer in self.customer_list[1:]:
            for i, vehicle in enumerate(self.vehicles):
                if vehicle.serve_customer(customer, i):
                    break
            if not customer.is_served:
                for i, vehicle in enumerate(self.vehicles):
                    if vehicle.serve_customer_force(customer, i):
                        break
        for vehicle in self.vehicles:
            if vehicle.last_service_time == 0:
                continue
            vehicle.return_home()
            self.vehicles_used += 1

    def generate_random_neighbour(self):
        rand_cust = self.customer_list[random.random(0, len(self.customer_list))]
        current_serving_vehicle = self.vehicles[rand_cust.vehicle_num]
        current_serving_vehicle.remove_customer(rand_cust)


        while not rand_cust.is_served:
            vehicle_num = random.random(0, len(self.vehicles))
            vehicle = self.vehicles[vehicle_num]
            if vehicle.last_service_time != 0:
                vehicle.try_to_serve_customer(rand_cust, i)

    def get_output(self):
        dist = 0
        result = ""
        i = 1
        for vehicle in self.vehicles:
            if vehicle.last_service_time == 0:
                continue
            vehicle.return_home()
            dist += vehicle.total_distance
            result += f'{i}: '
            for node in vehicle.service_route:
                result += f'{node[0].cust_no}({node[1]})->'
            result = result[:-2] + '\n'
            i += 1
        return f'{i-1}\n{result}{dist}'

def load_from_file(filepath):
    i = 0
    customer_list = []
    num_vehicles = 0
    capacity = 0

    with open(filepath) as f:
        line = f.readline()
        while line:
            if not line.strip(): # skip empty lines
                line = f.readline()
                continue

            if i == 2: # number of vehicles and capacity
                params = [int(p) for p in line.split()]
                num_vehicles = params[0]
                capacity = params[1]
            elif i >= 5: # customer info
                params = [int(p) for p in line.split()]
                customer_list.append(Customer(*params))

            i += 1
            line = f.readline()

    return Instance(num_vehicles, capacity, customer_list)