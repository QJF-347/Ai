import random

def generate(maze, start=(0, 0)):
    directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
    width, height = len(maze[0]), len(maze)
    
    def carve(x, y):
        maze[y][x] = 0  # Mark the current cell as open
        random.shuffle(directions)  # Shuffle directions to randomize paths
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                # Carve a path between the current cell and the neighbor cell
                maze[y + dy // 2][x + dx // 2] = 0
                carve(nx, ny)

    
    
    carve(start[1], start[0])
    return maze

# Create the maze grid
maze = [[1 for _ in range(20)] for _ in range(20)]
maze = generate(maze)

# Print the maze
for row in maze:
    print("".join(str(cell) for cell in row))
