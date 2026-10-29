"""Graph algorithms."""
from collections import deque

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
