import heapq

def heuristic(a,b):
    return abs(a[0] + abs(a[1] - b[1]))

def best_fs(grid,start,goal):
    open_list=[]
    heapq.heappush(open_list, (0,start))
    visited=set()
    visited.add(start)
    path=[]
    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    while open_list:
        current_priority, current_node=heapq.heappop(open_list)
        path.append(current_node)

        if current_node==goal:
            return path
        

        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] != 1 and neighbor not in visited:
                    visited.add(neighbor)
                    priority=heuristic(neighbor, goal)
                    heapq.heappush(open_list, (priority, neighbor))
    return None

grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start=(0,0)
goal=(3,4)
path = best_fs(grid,start,goal)
print("path found: ",path)