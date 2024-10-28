import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def AStarSearch(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_cost = {start: 0}
    came_from = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:
        current_f_cost, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]
        
        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])
            
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] != 1:
                    tentative_g_cost = g_cost[current_node] + 1
                    
                    if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                        g_cost[neighbor] = tentative_g_cost
                        f_cost = tentative_g_cost + heuristic(neighbor, goal)
                        heapq.heappush(open_list, (f_cost, neighbor))
                        came_from[neighbor] = current_node

    return None

grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4,4)

path = AStarSearch(grid, start, goal)
print("Path found:", path)
