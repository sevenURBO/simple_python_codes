#creating grid and filling with zeros
def create_grid(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid

#printing grid in different rows
def print_grid(grid):
    for row in grid:
        print(row)


grid = create_grid(5, 5)

print_grid(grid)
