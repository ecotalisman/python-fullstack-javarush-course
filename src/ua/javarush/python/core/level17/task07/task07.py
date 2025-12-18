# Adam's Morning: Checking for an Edge

# Write a function to check whether an edge exists between two vertices in a graph
# represented as an adjacency matrix.
# The function should take the adjacency matrix and two vertex indices and return True
# if an edge exists between the vertices, and False otherwise.

### 🇺🇦 Ukrainian version:

# Ранок Адама: шукаємо ребро

# Напишіть функцію для перевірки наявності ребра між двома вершинами в графі,
# представленому у вигляді матриці суміжності.
# Функція повинна приймати матрицю суміжності та два індекси вершин і повертати True,
# якщо між вершинами існує ребро, і False в іншому випадку.

def has_edge(matrix, vertex1, vertex2):
    # Write your code here
    n = len(matrix)
    if not (0 <= vertex1 < n and 0 <= vertex2 < n):
        return False
    return matrix[vertex1][vertex2] != 0

# Example usage:
adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(has_edge(adj_matrix, 0, 1))  # True
print(has_edge(adj_matrix, 0, 2))  # False
