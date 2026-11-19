"""Closed interval algorithms."""
from collections.abc import Iterable


def merge_intervals(intervals: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return the sorted union of closed intervals. O(n log n) time, O(n) space."""
    merged: list[tuple[int, int]] = []
    for start, end in sorted(intervals):
        if start > end:
            raise ValueError("interval start must be at or before its end")
        if merged and start <= merged[-1][1]:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))
    return merged
