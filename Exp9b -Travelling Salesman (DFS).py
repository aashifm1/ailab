graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
n = len(graph)

def dfs_tsp(graph):
    shortest_path = None
    min_cost = float('inf')
    
    def dfs(current_city, visited, cost):
        nonlocal shortest_path, min_cost
        
        if len(visited) == n:
            cost += graph[current_city][visited[0]]
            if cost < min_cost:
                min_cost = cost
                shortest_path = visited + [visited[0]]
            return
        
        for next_city in range(n):
            if next_city not in visited:
                new_visited = visited + [next_city]
                new_cost = cost + graph[current_city][next_city]
                dfs(next_city, new_visited, new_cost)
    
    for start_city in range(n):
        dfs(start_city, [start_city], 0)
    
    return shortest_path, min_cost

shortest_path, cost = dfs_tsp(graph)
print(f"Shortest path is {shortest_path} with a cost of {cost}")
