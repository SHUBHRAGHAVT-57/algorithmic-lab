"""Heap algorithms."""
from collections.abc import Iterable
from heapq import heappush, heapreplace


def k_largest(values: Iterable[int], k: int) -> list[int]:
    """Return up to k values in descending order, retaining duplicates."""
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k < 0:
        raise ValueError("k must be nonnegative")
    if k == 0:
        return []

    largest: list[int] = []
    for value in values:
        if len(largest) < k:
            heappush(largest, value)
        elif value > largest[0]:
            heapreplace(largest, value)
    return sorted(largest, reverse=True)
