import sys

data = sys.stdin.read().split()
grid = []
current_output = "-1"
current_depth = 0
visited = set()

def new_point(row, col):
    _new_list = []
    _current_value = int(grid[row][col])

    #Add new coordinates if valid for +- active value
    if (row + _current_value) != (row) and (row + _current_value) <= int(data[0]):
        _new_list.append([str(row + _current_value),str(col)])

    if (row - _current_value) != (row) and (row - _current_value) >= 0:
        _new_list.append([str(row - _current_value),str(col)])

    if (col + _current_value) != (col) and (col + _current_value) <= int(data[1]):
        _new_list.append([str(row), str(col + _current_value)])

    if (col - _current_value) != (col) and (col - _current_value) >= 0:
        _new_list.append([str(row), str(col - _current_value)])
    return _new_list

#Move to the next place
def goto_next(row, col):
    stack = [[str(row),str(col)]]
    while stack:
        active = stack.pop()
        if active not in visited:
            visited.add(active)
            _new_point(active[0], active[1])
            
            

#Seperate row numbers to a list in a list
for row in range(2, len(data)):
    _temp_data = []
    _target_row = str(data[row])
    for integer in range(len(_target_row)):
        _temp_data.append(_target_row[integer])
    grid.append(_temp_data)