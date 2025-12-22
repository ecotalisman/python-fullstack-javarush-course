# Shortest Path Between Cities (Dijkstra)

# Write a function to find the shortest path between two cities in a transportation network
# using Dijkstra's algorithm.
# The function should return the shortest path and its total cost.

### 🇺🇦 Ukrainian version:

# Шлях між містами

# Напишіть функцію для знаходження найкоротшого шляху між двома містами в транспортній мережі
# з використанням алгоритму Дейкстри.
# Функція повинна повертати найкоротший шлях та його вартість.


import heapq

def dijkstra(graph, start, end):
    # Write your code here
    distances = {v: float("inf") for v in graph}
    distances[start] = 0
    parents = {v: None for v in graph}
    pq = [(0, start)]

    while pq:
        cur_dist, cur_v = heapq.heappop(pq)

        if cur_dist > distances[cur_v]:
            continue

        if cur_v == end:
            break

        for nbr, w in graph[cur_v].items():
            new_dist = cur_dist + w

            if new_dist < distances[nbr]:
                distances[nbr] = new_dist
                parents[nbr] = cur_v

                heapq.heappush(pq, (new_dist, nbr))

    if distances[end] == float("inf"):
        return float("inf"), []

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parents[cur]
    path.reverse()

    return distances[end], path

# Example graph: a dictionary where the key is a city, and the value is a dictionary of neighbors and distances
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Example usage of the function:
start_city = 'A'
end_city = 'D'
distance, path = dijkstra(graph, start_city, end_city)
print(f"The shortest path from {start_city} to {end_city} costs {distance} and goes through {path}.")
