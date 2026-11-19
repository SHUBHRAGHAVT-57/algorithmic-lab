"""Graph algorithms."""
from collections import deque
from heapq import heappop, heappush

def bfs_shortest_paths(adjacency: dict[int, list[int]], source: int) -> dict[int, int]:
    """Shortest hop distances in an unweighted directed graph. O(V+E)."""
    distances = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in adjacency.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances


def dijkstra_shortest_paths(
    adjacency: dict[int, list[tuple[int, int]]], source: int
) -> dict[int, int]:
    """Return shortest reachable distances in a directed graph with nonnegative integer weights."""
    for edges in adjacency.values():
        for _, weight in edges:
            if isinstance(weight, bool) or not isinstance(weight, int):
                raise TypeError("edge weights must be integers")
            if weight < 0:
                raise ValueError("edge weights must be nonnegative")

    distances = {source: 0}
    queue = [(0, source)]
    while queue:
        distance, node = heappop(queue)
        if distance != distances[node]:
            continue
        for neighbor, weight in adjacency.get(node, ()):
            candidate = distance + weight
            previous = distances.get(neighbor)
            if previous is None or candidate < previous:
                distances[neighbor] = candidate
                heappush(queue, (candidate, neighbor))
    return distances
