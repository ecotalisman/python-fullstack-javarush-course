# Connected Graph: BFS Version

# Write a function to check whether a graph is connected using BFS.
# The function should take a graph represented as adjacency lists and return True
# if the graph is connected, and False otherwise.

### 🇺🇦 Ukrainian version:

# Зв'язний граф: BFS-версія

# Напишіть функцію для перевірки, чи є граф зв'язним з використанням BFS.
# Функція повинна приймати граф у вигляді списків суміжності та повертати True, якщо граф зв'язний,
# і False в іншому випадку.


from collections import deque

def is_connected(graph):
    # Write your code here
    if not graph:
        return False

    visited = set()
    start = next(iter(graph))
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)

    return len(visited) == len(graph)

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
print(is_connected(graph))  # True
