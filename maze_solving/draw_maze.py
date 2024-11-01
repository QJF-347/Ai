import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("maze")


def load_maze(filename):
    with open('maze', 'r' ) as file :
        return [list(line.strip()) for line in file]
    
run = True

while run:
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    load_maze(1)
pygame.quit()