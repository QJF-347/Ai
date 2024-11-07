import pygame


pygame.init()
WIDTH, HEIGHT = 800, 800
RES = (WIDTH, HEIGHT)
ROWS, COLUMNS = 8, 8
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (20, 200, 0)
CELLW, CELLH = WIDTH // COLUMNS, HEIGHT // ROWS

board = [[0 for _ in range(COLUMNS)]for _ in range(ROWS)]
board[4][3] = 'wq'
board[2][7] = 'wq'

def drawboard(screen, rows=ROWS, cols=COLUMNS):
    for row in range(rows):
        for col in range(cols):
            color = GREEN if (row + col) % 2 != 0 else WHITE
            pygame.draw.rect(screen, color, (row * CELLH, col * CELLW, (row + 1) * CELLH, (col + 1) * CELLW))
            if board[row][col] != 0:
                path = 'img/bq.png' if board[row][col] == 'bq' else 'img/wq.png'
                image = pygame.image.load(path) 
                image = pygame.transform.scale(image, (CELLW, CELLH))
                screen.blit(image, (row * CELLH, col * CELLW))



def main():
    running = True
    screen = pygame.display.set_mode(RES)
    
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running  =False
        drawboard(screen,)
        pygame.display.flip()
    pygame.quit()
    




main()