import random
maze = [[1 for _ in range(60)] for _ in range(60)]

def generate(maze = maze, start=(0, 0)):
    directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
    width, height = len(maze[0]), len(maze)

    def pather(x, y):
        maze[x][y] = 0
        random.shuffle(directions)
        for dx, dy in directions:
            cx, cy = x+dx, y+dy
            if 0 <= cx < width and 0 <= cy < height and maze[cx][cy] == 1:
                maze[x + dx //2][y + dy //2] = 0
                pather(cx, cy)    
    pather(start[0], start[1])   
    return maze

maze = generate()
for m in maze:
    print(str(m).replace(',', '').replace('[', '').replace(']', '').replace(' ', ''))