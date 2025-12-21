# Shortest Path: BFS Version

# Write a function to find the shortest path from a start vertex to a target vertex
# in an undirected graph using BFS.
# The function should return a list of vertices that make up the shortest path.

### 🇺🇦 Ukrainian version:

# Найкоротший шлях: BFS-версія

# Напишіть функцію для пошуку найкоротшого шляху від початкової вершини до цільової
# в неорієнтованому графі з використанням BFS.
# Функція повинна повертати список вершин, що складають найкоротший шлях.


from collections import deque

def find_shortest_path(graph, start, goal):
    # Write your code here
    if start == goal:
        return [start]

    visited = {start}
    parents = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
                parents[nbr] = node

                if nbr == goal:
                    path = []
                    cur = goal
                    while cur is not None:
                        path.append(cur)
                        cur = parents[cur]
                    path.reverse()

                    return path

    return []

# Example for usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
print(find_shortest_path(graph, start, goal))
