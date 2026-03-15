import sys

data = sys.stdin.read().split()
grid = []
current_depth = -1
visited = set()

#Add new coordinates if valid for +- active value
def new_point(row, col):
    _new_list = []
    _current_value = int(grid[row][col])

    if (row + _current_value) != (row) and (row + _current_value) < int(data[0]):
        if ((row + _current_value), col) not in visited:
            visited.add(((row + _current_value), col))
            _new_list.append([(row + _current_value),col])

    if (row - _current_value) != (row) and (row - _current_value) >= 0:
        if ((row - _current_value), col) not in visited:
            visited.add(((row - _current_value), col))
            _new_list.append([(row - _current_value),col])

    if (col + _current_value) != (col) and (col + _current_value) < int(data[1]):
        if (row, (col + _current_value)) not in visited:
            visited.add((row, (col + _current_value)))
            _new_list.append([row, (col + _current_value)])

    if (col - _current_value) != (col) and (col - _current_value) >= 0:
        if (row, (col -_current_value)) not in visited:
            visited.add((row, (col - _current_value)))
            _new_list.append([row, (col - _current_value)])
        
    return _new_list

#Move to the next place
def next_depth(_next):
    queue = _next
    stack = []
    while queue:
        current_cord = queue.pop()
        new_cord = new_point(current_cord[0], current_cord[1])
        for i in range(len(new_cord)):
            stack.append(new_cord[i])
    return stack
            

#Map out the input to a 2D list.
for row in range(2, len(data)):
    _temp_data = []
    _target_row = str(data[row])
    for integer in range(len(_target_row)):
        _temp_data.append(_target_row[integer])
    grid.append(_temp_data)

start = [[0,0]]

while (data[0], data[1]) not in visited and start:
    current_depth +=1
    start = next_depth(start)
if ((int(data[0])-1), (int(data[1])-1)) in visited:
    print(str(current_depth))
else:
    print("-1")