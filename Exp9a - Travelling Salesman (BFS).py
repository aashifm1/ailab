from collections import deque

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
n = len(graph)

def bfs_tsp(graph):
    shortest_path = None
    min_cost = float('inf')
    
    for start_city in range(n):
        queue = deque([(start_city, [start_city], 0)])
        
        while queue:
            current_city, visited, cost = queue.popleft()
            
            if len(visited) == n:
                cost += graph[current_city][start_city]
                if cost < min_cost:
                    min_cost = cost
                    shortest_path = visited + [start_city]
                continue
            
            for next_city in range(n):
                if next_city not in visited:
                    new_visited = visited + [next_city]
                    new_cost = cost + graph[current_city][next_city]
                    queue.append((next_city, new_visited, new_cost))
                    
    return shortest_path, min_cost

shortest_path, cost = bfs_tsp(graph)
print(f"Shortest path is {shortest_path} with a cost of {cost}")
