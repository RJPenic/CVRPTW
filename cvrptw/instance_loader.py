
class Customer:
    def __init__(self, cust_no, x, y, demand, ready_time, due_date, service_time):
        self.cust_no = cust_no
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_time = service_time

    def __str__(self):
        return f'Customer NO. : {self.cust_no}; X : {self.x}; Y : {self.y}; Demand : {self.demand}; Ready Time : {self.ready_time}; Due Date : {self.due_date}; Service Time : {self.service_time}'

class Instance:
    def __init__(self, num_vehicles, capacity, customer_list):
        assert (
            num_vehicles > 0 and capacity > 0
        ), f'Number of vehicles and their capacity must be positive! {num_vehicles}, {capacity}'
        self.num_vehicles = num_vehicles
        self.capacity = capacity

        customer_list.sort(key = lambda c: c.cust_no)
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