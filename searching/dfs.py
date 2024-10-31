

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

def dfs(graph=graph):
    frontier = ['A'] # stack
    explored = []
    goal = 'L'
    
    while frontier: 
        current_node = frontier.pop()
        if current_node == goal:
            print("Explored =>" , explored)
            print('goal found =>', goal)
            break
        if current_node not in explored:
            explored.append(current_node)
            for child in graph[current_node]:
                frontier.append(child)
        else:
            print("Gola not found")
    
dfs()