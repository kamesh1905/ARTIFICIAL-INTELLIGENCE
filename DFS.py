

def dfs(graph, node, visited=[]):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Sample graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

dfs(graph, 'A')
