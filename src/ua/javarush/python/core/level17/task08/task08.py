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

def adjacency_matrix_to_list(matrix):
    # Write your code here
    return [[j for j, w in enumerate(row) if w != 0] for row in matrix]


# Example usage
matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print(adjacency_matrix_to_list(matrix))
