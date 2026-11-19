# Reference algorithms

Import the functions from `algolab` with `PYTHONPATH` set to the repository's `python` directory. [Test and environment instructions](../README.md#run-tests)

## Inorder tree traversal

`TreeNode(value, left=None, right=None)` represents a binary tree with integer values. `inorder_values(root)` returns the values in left subtree, root, right subtree order. It accepts any finite acyclic binary tree and returns `[]` for `None`. The traversal leaves node values and links intact.

The stack holds each ancestor until its left subtree has been visited. Each node is pushed and popped once, so the traversal takes O(n) time and O(h) auxiliary space for n nodes and tree height h, excluding the returned list. An explicit stack supports trees deeper than Python's recursion limit.

```python
from algolab import TreeNode, inorder_values

root = TreeNode(2, TreeNode(4), TreeNode(1))
assert inorder_values(root) == [4, 2, 1]
```

[Implementation](../python/algolab/trees.py)

## K largest values

`k_largest(values, k)` accepts a finite iterable of integers, including a one-pass iterator. It returns the largest min(k, n) values from n items in descending order, retaining duplicates. A zero count returns an empty list without reading the input. Negative counts raise `ValueError`. Boolean and other non-integer counts raise `TypeError`.

A min-heap holds the largest values seen so far. When it reaches k entries, only a value greater than the heap's minimum replaces an entry. For k > 0, the scan and final sort take O(n log(r + 1)) time and O(r) space for r = min(k, n).

```python
from algolab import k_largest

assert k_largest(iter([4, -1, 4, 2]), 3) == [4, 4, 2]
```

[Implementation](../python/algolab/heaps.py)

## Dijkstra shortest paths

`dijkstra_shortest_paths(adjacency, source)` takes a directed graph with integer vertex IDs. Each adjacency list contains `(neighbor, weight)` pairs. The result includes the source at distance zero and every reachable vertex, including neighbors without adjacency lists. Self-loops, parallel edges, and zero-weight cycles are valid.

The algorithm validates all edge weights before searching, including edges outside the source's component. A negative weight raises `ValueError`. A boolean or other non-integer weight raises `TypeError`. The minimum-distance heap expands a vertex only when its queued distance matches its best known distance. Each successful relaxation pushes a new entry. With V vertices and E edges, validation and search take O((V + E) log(V + E + 1)) time and O(V + E) space.

```python
from algolab import dijkstra_shortest_paths

graph = {0: [(1, 10), (2, 1)], 2: [(1, 2)], 9: []}
assert dijkstra_shortest_paths(graph, 0) == {0: 0, 1: 3, 2: 1}
```

[Implementation](../python/algolab/graphs.py)

## Merge closed intervals

`merge_intervals(intervals)` takes a finite iterable of closed integer intervals as `(start, end)` pairs. The result is a sorted list of disjoint intervals with the same union. Point intervals are valid, intervals sharing an endpoint merge, and empty input returns `[]`. An interval whose start exceeds its end raises `ValueError`.

The algorithm sorts a copy of the input and scans it in start order. Each new interval can overlap only the last interval in the output so far. Sort and scan take O(n log n) time and O(n) space.

```python
from algolab import merge_intervals

assert merge_intervals([(5, 7), (1, 3), (3, 5), (9, 9)]) == [(1, 7), (9, 9)]
```

[Implementation](../python/algolab/intervals.py)

## Longest common subsequence length

`longest_common_subsequence_length(left, right)` returns the number of Unicode code points in a longest shared subsequence. Matches preserve their order and may have gaps. The function compares code points as given, without Unicode normalization. Empty input on either side returns zero.

For matching code points, the result for the two prefixes is one plus the value for the prefixes omitting both code points. Otherwise it is the larger result from omitting one side. The algorithm keeps a row for the shorter string and saves the previous row's diagonal value before overwriting it. For nonempty lengths m and n, it takes O(mn) time and O(min(m, n)) auxiliary space.

```python
from algolab import longest_common_subsequence_length

assert longest_common_subsequence_length("abcde", "ace") == 3
```

[Implementation](../python/algolab/strings.py)
