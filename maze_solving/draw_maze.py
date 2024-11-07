import pygame
from maze_solver import bfs, dfs

pygame.init()
  
WIDTH, HEIGHT = 600, 600

CELL_SIZE = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("maze")


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


def load_maze(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

maze = load_maze('maze_solving/mazes/maze5.txt') 
start, goal = find_start_goal(maze)

def draw_maze(screen=screen, maze=maze, path=[], visited=[]):
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
            
            pygame.draw.rect(screen, color,(col_idx * CELL_SIZE, row_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK,(col_idx * CELL_SIZE, row_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1 )

    for (x, y) in visited:
        pygame.draw.rect(screen, YELLOW, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
    
    for (x, y) in path:
        pygame.draw.rect(screen, BLUE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
        

def main():
    run =  True
    FPS = 100
    generator = bfs(maze, start, goal)
    clock = pygame.time.Clock()
    
    
    try:
        # Fetch the first path and visited nodes from the generator
        path, visited = next(generator)
    except StopIteration:
        path, visited = [], [] 
    
    
    
    while run:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        try:
            path, visited = next(generator)
            pass
        except StopIteration:
            pass
            
        
        draw_maze(screen, maze, path ,visited)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()