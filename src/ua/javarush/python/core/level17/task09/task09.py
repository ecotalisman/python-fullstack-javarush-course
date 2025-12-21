# Escaping the Maze

# Given a 2D array representing a maze where 0 is a walkable cell and 1 is a wall,
# write a function to find a path from a start point to an end point using DFS.
# The start and end points are given as coordinates.

### 🇺🇦 Ukrainian version:

# Вихід з лабіринту

# Дано двовимірний масив, що представляє лабіринт, де 0 – це прохідна клітина, а 1 – стіна.
# Напишіть функцію для знаходження шляху від початкової точки до кінцевої з використанням DFS.
# Початкова і кінцева точки задані координатами.

def find_path(maze, start, end):
    # Write your code here
    stack = [start]
    visited = {start}
    parent = {start: None}

    while stack:
        x, y = stack.pop()

        if (x, y) == end:
            path = []
            cur = end
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            nxt = (nx, ny)

            rows, cols = len(maze), len(maze[0])

            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and maze[nx][ny] == 0
                and nxt not in visited
            ):
                visited.add(nxt)
                parent[nxt] = (x, y)
                stack.append(nxt)

    return []

# Example usage
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)
path = find_path(maze, start, end)
print(path)
