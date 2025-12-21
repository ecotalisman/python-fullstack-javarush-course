# Connected Graph (DFS)

# Write a function to check whether a graph is connected using DFS.
# The function should take a graph represented as adjacency lists and return True
# if the graph is connected, and False otherwise.

### 🇺🇦 Ukrainian version:

# Зв'язний граф

# Напишіть функцію для перевірки, чи є граф зв'язним, з використанням DFS.
# Функція повинна приймати граф у вигляді списків суміжності і повертати True, якщо граф зв'язний,
# і False в іншому випадку.

def dfs(graph, visited, node):
    # Write your code here
    visited.add(node)
    for neigh in graph.get(node, []):
        if neigh not in visited:
            dfs(graph, visited, neigh)

def is_connected(graph):
    # Write your code here
    if not graph:
        return False
    visited = set()
    start = next(iter(graph))
    dfs(graph, visited, start)

    return len(visited) == len(graph)

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
print(is_connected(graph))  # Output: True
