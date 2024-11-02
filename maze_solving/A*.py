import heapq
import pygame

# Define colors for drawing
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

CELL_SIZE = 30
WIDTH, HEIGHT = 600, 600

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm for solving a maze
def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    heap = []
    
    # g_score: cost from start to the current node
    g_score = {start: 0}
    
    # f_score: g_score + heuristic (Manhattan distance)
    f_score = {start: heuristic(start, goal)}
    
    # Push the start node into the priority queue with its f_score
    heapq.heappush(heap, (f_score[start], start))
    
    came_from = {}
    visited = set()
    
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    while heap:
        _, current = heapq.heappop(heap)  # Pop the node with the lowest f_score
        visited.add(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], visited  # Return the path and visited nodes
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                maze[neighbor[0]][neighbor[1]] != '1' and neighbor not in visited):
                
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(heap, (f_score[neighbor], neighbor))
                    yield list(came_from.keys()), list(visited)  # Yield to visualize progress
                    
    return None, visited

# Load maze function
def load_maze(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

# Automatically find start and goal positions
def find_start_goal(maze):
    start = None
    goal = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'G':
                goal = (r, c)
    return start, goal

# Drawing function for maze, path, and visited nodes
def draw_maze(screen, maze, path=[], visited=[]):
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == '1':
                color = WHITE
            elif cell == "S":
                color = RED
            elif cell == "G":
                color = GREEN
            else:
                color = BLACK
            
            pygame.draw.rect(screen, color, (col_idx * CELL_SIZE, row_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (col_idx * CELL_SIZE, row_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    for (x, y) in visited:
        pygame.draw.rect(screen, YELLOW, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    for (x, y) in path:
        pygame.draw.rect(screen, BLUE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

# Main function for running the pygame window
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("A* Maze Solver")
    
    # Load your maze from a file
    maze = load_maze('maze_solving/mazes/maze2.txt')
    
    # Automatically find start and goal in the maze
    start, goal = find_start_goal(maze)
    if not start or not goal:
        print("Start or goal position not found in the maze!")
        return
    
    clock = pygame.time.Clock()
    generator = astar(maze, start, goal)
    
    run = True
    path = []
    visited = []
    
    while run:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        try:
            # Get the next step in the A* search
            path, visited = next(generator)
        except StopIteration:
            pass
            
        draw_maze(screen, maze, path, visited)
        pygame.display.flip()
        clock.tick(10)  # Slow down the visualization to 10 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
