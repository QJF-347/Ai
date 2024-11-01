import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("maze")


def load_maze(filename):
    with open(filename , 'r') as file :
        return [list(line.strip()) for line in file]
run = True

while run:
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    print(load_maze('maze.txt'))
pygame.quit()