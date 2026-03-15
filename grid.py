import sys

data = sys.stdin.read().split()
grid = []
current_output = "-1"
current_depth = 0
visited = set()

#Seperate row numbers to a list in a list
for row in range(2, len(data)):
    _temp_data = []
    _target_row = str(data[row])
    for integer in range(len(_target_row)):
        _temp_data.append(_target_row[integer])
    grid.append(_temp_data)

#Move to the next place
def goto_next(row, col):
    stack = [[str(row),str(col)]]
    while stack:
        active = stack.pop()
        if active not in visited:
            visited.add(active)
            _new_list = []

            #Add new coordinates if valid for +- active value
            if (int(active[0])+int(grid[row][col])) <= int(data[0]):
                _new_list.append([(int(active[0])+int(grid[row][col])),col])

            if (int(active[0])-int(grid[row][col])) >= 0:
                new_list.append([(int(active[0])-int(grid[row][col])),col])

            if (int(active[1])+int(grid[row][col])) <= int(data[1]):
                _new_list.append([row, int(active[1])+int(grid[row][col])])

            if (int(active[1])-int(grid[row][col])) >= 0:
                _new_list.append([row, int(active[1])-int(grid[row][col])])
            