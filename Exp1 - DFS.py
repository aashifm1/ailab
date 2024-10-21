graph = {
'A':['B','C'],
'B':['D'],
'C':['D','E'],
'D':['E'],
'E':[]
}
visited=set()
def dfs(visited, graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
print("Following is the DFS")
dfs(visited, graph, 'A')