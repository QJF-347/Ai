from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    came_from = {}  
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  
    goal_reached = False  
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
           
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            queue = []
            goal_reached = True 
            yield path[::-1], visited  
            return  
        
        visited.add(current)
        
        # Explore neighbors
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                maze[neighbor[0]][neighbor[1]] != '1' and neighbor not in visited):
                
                queue.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current 

      
        if not goal_reached:
            path = []
            temp = current
            while temp in came_from:
                path.append(temp)
                temp = came_from[temp]
            path.append(start)
            yield path[::-1], visited  


def dfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    stack = deque([start])
    visited = set()
    came_from = {}
    
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    goal_reached = False  
    
    while stack:
        current = stack.pop() 
        if current == goal:
           
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            goal_reached = True  
            yield path[::-1], visited  
            return 

        visited.add(current)


        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                maze[neighbor[0]][neighbor[1]] != '1' and neighbor not in visited):
                
                stack.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current 
            
           
            if not goal_reached:
                path = []
                temp = current
                while temp in came_from:
                    path.append(temp)
                    temp = came_from[temp]
                path.append(start)
                yield path[::-1], visited  
