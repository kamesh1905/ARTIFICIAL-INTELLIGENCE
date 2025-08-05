

import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan Distance

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = [(0 + heuristic(start, goal), 0, start)]  # (f, g, node)
    came_from = {}
    visited = set()

    while open_set:
        f, g, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        visited.add(current)
        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:  # Up, down, left, right
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if neighbor in visited:
                    continue
                new_g = g + 1
                heapq.heappush(open_set, (new_g + heuristic(neighbor, goal), new_g, neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current
    return None  # No path found

# Example grid (0 = walkable, 1 = wall)
grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = astar(grid, start, goal)
print("Path:", path)
