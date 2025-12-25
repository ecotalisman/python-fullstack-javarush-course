# Topological Sorting (DFS)

# You have a list of tasks and their dependencies. Write a function to determine
# the execution order of tasks using topological sorting with Depth-First Search (DFS).
# The function should return a list of tasks in the correct order.

### 🇺🇦 Ukrainian version:

# Топологічне сортування

# У вас є список задач та їх залежності. Напишіть функцію для визначення порядку виконання задач
# з використанням топологічного сортування через пошук у глибину (DFS).
# Функція повинна повертати список задач у правильному порядку.


# Helper function for DFS
from collections import defaultdict, deque

# Create adjacency list
graph = defaultdict(list)

# Visited nodes tracker
visited = set()
temp_marks = set()
stack = list()


def dfs(node):
    if node in temp_marks:
        raise ValueError("Graph is not a Directed Acyclic Graph (DAG)")

    if node not in visited:
        temp_marks.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        temp_marks.remove(node)
        visited.add(node)
        stack.append(node)


def topological_sort(tasks):
    # Write your code here
    all_nodes = set()

    graph.clear()
    visited.clear()
    temp_marks.clear()
    stack.clear()

    for task, dep in tasks:
        all_nodes.add(task)
        all_nodes.add(dep)
        graph[task].append(dep)

    for node in sorted(all_nodes):
        if node not in visited:
            dfs(node)

    return stack[::-1]


# Example usage:
tasks = [('a', 'b'), ('b', 'c'), ('c', 'd')]
print(topological_sort(tasks))  # Output: ['a', 'b', 'c', 'd']
