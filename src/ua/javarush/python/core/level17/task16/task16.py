# Sorting Packages (Topological Sort with DFS)

# Write a function to order packages so that all dependencies are installed
# before installing the package itself.
# Use topological sorting with Depth-First Search (DFS).
# The function should return a list of packages in the correct installation order.

### 🇺🇦 Ukrainian version:

# Сортування сміття

# Напишіть функцію для впорядкування пакетів так, щоб усі залежності були встановлені
# перед встановленням самого пакету.
# Використовуйте алгоритм топологічного сортування через пошук в глибину (DFS).
# Функція повинна повертати список пакетів у правильному порядку встановлення.


dependency_graph = dict()
visited = set()
temp_marked = set()
result = list()

def dfs(package):
    if package in temp_marked:
        raise ValueError("Cycle detected!")
    if package not in visited:
        temp_marked.add(package)
        for dep in dependency_graph.get(package, []):
            dfs(dep)
        temp_marked.remove(package)
        visited.add(package)
        result.append(package)

def topological_sort(packages):
    # Write your code here
    all_nodes = set()

    dependency_graph.clear()
    visited.clear()
    temp_marked.clear()
    result.clear()

    for pack, deps in packages:
        all_nodes.add(pack)
        dependency_graph.setdefault(pack, []).extend(deps)

        for dep in deps:
            all_nodes.add(dep)

    for node in sorted(all_nodes):
        if node not in visited:
            dfs(node)

    return result

# Example usage:
packages = [
    ('a', ['b', 'c']),
    ('b', ['c', 'd']),
    ('c', ['d']),
    ('d', [])
]

print(topological_sort(packages))
# Output: ['d', 'c', 'b', 'a']
