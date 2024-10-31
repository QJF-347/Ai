

graph = {
    'A':['B', 'C', 'D'], 
    'B':['E', 'F'], 
    'C':['G'], 
    'D':['H', 'I'], 
    'E':['M'],
    'F':[], 
    'G':['J', 'K'], 
    'H':[],
    'I':[],
    'J':['L', ],
    'K':[], 
    'L':[], 
    'M':[]
}

def bfs(graph=graph):
    frontier = ['A'] # queue
    explored = []
    goal = 'L'
    
    while frontier:
        current_node = frontier.pop(0)
        if current_node == goal:
            print("Explored =>" , explored)
            print('goal found =>', goal)
            break
        if current_node not in explored:
            explored.append(current_node)
            
            for child in graph[current_node]:
                if child not in explored and child not in frontier:
                    frontier.append(child)
        else:
            print("Goal not found")
bfs()