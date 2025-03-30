import random

# Initialize the grid with random noise
def fill_cell_grid_with_noise(width, height, chance_of_wall):
    grid = []
    for y in range(height):  # Iterate over height first
        row = []
        for x in range(width):  # Iterate over width
            row.append(random.random() >= chance_of_wall)
        grid.append(row)
    return grid

# Count the number of wall neighbors for a given cell
def count_wall_neighbors(cell_grid, x, y):
    width, height = len(cell_grid[0]), len(cell_grid)
    neighbors = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            x1, y1 = x + dx, y + dy
            if 0 <= x1 < width and 0 <= y1 < height and cell_grid[y1][x1]:
                neighbors += 1
    return neighbors

# Apply the cellular automata rules to smooth the grid
def apply_rules(cell_grid):
    width, height = len(cell_grid[0]), len(cell_grid) 
    num_wall_neighbors=[]
    for y in range(height):
        row = []
        for x in range(width):
            row.append(count_wall_neighbors(cell_grid, x, y))
        num_wall_neighbors.append(row)
    for y in range(height):
        for x in range(width):
            neighbors = num_wall_neighbors[y][x]
            if cell_grid[y][x] and neighbors < 4:
                cell_grid[y][x] = False
            elif not cell_grid[y][x] and neighbors >= 5:
                cell_grid[y][x] = True
    return cell_grid



width, height = 25, 15  # Grid dimensions
chance_of_wall = 0.45   # Probability of a cell starting as a wall

# Generate initial grid and apply smoothing rules
cell_grid = fill_cell_grid_with_noise(width, height, chance_of_wall)

# Display initial grid
print("Initial Grid:")
for row in cell_grid:
    line=""
    for i in row:
        if i==True:
            line+="#"
        else:
            line+="."
    print(line)

# Apply rules multiple times to refine the cave structure
for _ in range(3):  # Adjust iterations for better smoothing
    cell_grid = apply_rules(cell_grid)

# Display the generated cave grid
print("\nFinal Grid:")
for row in cell_grid:
    line=""
    for i in row:
        if i==True:
            line+="#"
        else:
            line+="."
    print(line)
