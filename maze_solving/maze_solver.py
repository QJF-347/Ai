from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start, ])
    visited = set()
    came_from = {}
    
    directions = (0, 1), (1, 0), (-1, 0), (0, -1)
    
    while queue:
        current = queue.popleft() # first in fist out
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], visited
        
        visited.add(current)
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                maze[neighbor[0]][neighbor[1]] != '1' and neighbor not in visited):
                
                queue.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current 
                    
            path = []
            temp = current
            while temp in came_from:
                path.append(temp)
                temp = came_from[temp]
            path.append(start)
            yield path[::-1], visited 

def dfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    stack = deque([start, ])
    visited = set()
    came_from = {}
    
    directions = (0, 1), (1, 0), (-1, 0), (0, -1)
    
    while stack:
        current = stack.pop() # last in fist out
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], visited
        visited.add(current)

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                maze[neighbor[0]][neighbor[1]] != '1' and neighbor not in visited):
                
                stack.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current 
            
            path = []
            temp = current
            while temp in came_from:
                path.append(temp)
                temp = came_from[temp]
            path.append(start)
            yield path[::-1], visited 