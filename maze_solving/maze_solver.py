from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    came_from = {}  # This will store the path (the predecessor of each node)
    
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left
    
    while queue:
        current = queue.popleft()  # BFS: first in, first out
        
        if current == goal:
            # If goal is reached, reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], visited  # Return the complete path from start to goal
        
        visited.add(current)
        
        # Explore neighbors
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                maze[neighbor[0]][neighbor[1]] != '1' and neighbor not in visited):
                
                queue.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current  # Track the predecessor of the neighbor

        # For progress visualization/debugging, yield the current path from start to current node
        path = []
        temp = current
        while temp in came_from:
            path.append(temp)
            temp = came_from[temp]
        path.append(start)
        yield path[::-1], visited  # Yield the current partial path for visualization


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