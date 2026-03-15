import sys

data = sys.stdin.read().split()
houses = {}
_visited = set()
_countdown = 0

class House:
    
    def __init__(self):
        self.connecting = set()

    def set_connection(self, corded):
        self.connecting.add(corded) 


def control_connection(house):
    stack = [house]
    while stack:
        _checking = stack.pop()
        if _checking not in _visited:
            _visited.add(_checking)
            for neighbour in houses[_checking].connecting:
                if neighbour not in _visited:
                        stack.append(neighbour)

    #for connected in houses[house].connecting:
    #     if connected not in _visited:
    #          control_connection(connected)

if int(data[0]) == 1:
    print("Connected")
 
else:
    total_houses = int(data[0])
    number_of_cables = int(data[1])

    #Create all the existing houses.
    for i in range(total_houses):
        houses[(i+1)] = House()
    
    #Add the the connecting house to their set of connected
    for i in range(number_of_cables):
            houses[int(data[i * 2 + 2])].set_connection(int(data[i * 2 + 3]))
            houses[int(data[i * 2 + 3])].set_connection(int(data[i * 2 + 2]))
    
    #Controll connected to house 1
    control_connection(1)

    if int(data[0]) == len(_visited):
        print("Connected")
    
    else:
        countdown = int(data[0])

        for i in range(1,countdown+1):
            if i in _visited:
                continue
            else:
                print(str(i))
