from collections import deque

# Порядок по часовой стрелке: Right -> Down -> Left -> Up
CLOCKWISE = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs_clockwise(maze):
    start, goal = maze.start, maze.goal
    visited = {start}
    parent = {start: None}
    stack = [start]
    visited_order = [start]

    while stack:
        x, y = stack.pop()
        if (x, y) == goal:
            break
        for dx, dy in CLOCKWISE:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and maze.can_move(x, y, nx, ny):
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                stack.append((nx, ny))
                visited_order.append((nx, ny))

    if goal not in parent:
        return None, visited_order

    # восстановление пути
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path, visited_order


def bfs(maze):
    start, goal = maze.start, maze.goal
    visited = {start}
    parent = {start: None}
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break
        for dx, dy in CLOCKWISE:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and maze.can_move(x, y, nx, ny):
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    if goal not in parent:
        return None
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
