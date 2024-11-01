import pygame
from maze_solver import bfs, dfs

pygame.init()
  
WIDTH, HEIGHT = 600, 600

CELL_SIZE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("maze")

start = (19, 0)
goal = (5, 10)
def load_maze(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

maze = load_maze('maze_solving/mazes/maze2.txt') 
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
    path, visited = dfs(maze, start, goal)
    while run:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_maze(screen, maze, path if path else [], visited if visited else [])
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()