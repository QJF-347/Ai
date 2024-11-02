import heapq

def a_star(graph, start, goal):
    # Priority queue for the open set
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Dictionary to keep track of the cost to reach each node
    g_score = {start: 0}
    
    # Dictionary to keep track of the parent of each node (for reconstructing path)
    came_from = {}
    
    # Heuristic function: we use a simple constant heuristic for this example
    def heuristic(node, goal):
        return 0
    
    while open_list:
        # Get the node in open_list with the lowest f_score
        current_f, current = heapq.heappop(open_list)
        
        # If we reached the goal, reconstruct and return the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] 
        

        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight  
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
    
    return None


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 2), ('E', 4)],
    'C': [('A', 3), ('F', 6)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 4), ('D', 1), ('G', 1)],
    'F': [('C', 6)],
    'G': [('E', 1)],
}

start_node = 'A'
goal_node = 'G'

path = a_star(graph, start_node, goal_node)

print(f"Path from {start_node} to {goal_node}: {path}")
