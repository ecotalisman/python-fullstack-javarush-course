# Cities and Adjacency Lists

# You have Dijkstra's algorithm implemented for an adjacency matrix.
# Rewrite it for a graph given as an adjacency list.

### 🇺🇦 Ukrainian version:

# Міста і списки

# У вас є алгоритм Дейкстри, реалізований для матриці суміжності.
# Переробіть його для графа, заданого списком суміжності.


import heapq

def dijkstra(adj_list, start):
    # Write your code here
    distances = {v: float('inf') for v in adj_list}
    distances[start] = 0
    parents = {v: None for v in adj_list}
    pq = [(0, start)]

    while pq:
        cur_dist, cur_v = heapq.heappop(pq)

        if cur_dist > distances[cur_v]:
            continue

        for nbr, w in adj_list[cur_v]:
            new_dist = cur_dist + w

            if new_dist < distances[nbr]:
                distances[nbr] = new_dist
                parents[nbr] = cur_v

                heapq.heappush(pq, (new_dist, nbr))

    return distances, parents

# Example usage:
adj_list = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
start = 0
print(dijkstra(adj_list, start))
