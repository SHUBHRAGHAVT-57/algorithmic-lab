# Algorithmic Lab

A collection of nine Python reference algorithms for studying data structures and problem-solving techniques. Each implementation uses the standard library and has automated tests.

Maintained by [Shubh Raghav](https://github.com/SHUBHRAGHAVT-57).

## Implemented algorithms

| Topic | Implementation | Contract |
| --- | --- | --- |
| Arrays | [Two Sum](python/algolab/arrays.py) | Returns distinct matching indices or `None`. O(n) time and space. |
| Arrays | [Maximum Subarray](python/algolab/arrays.py) | Returns the largest nonempty contiguous sum. Raises `ValueError` for empty input. O(n) time. |
| Search | [Lower Bound](python/algolab/search.py) | Finds the first insertion position in ascending sorted input. O(log n) time. |
| Graphs | [BFS shortest paths](python/algolab/graphs.py) | Finds hop distances to reachable vertices. O(V + E) time. |
| Graphs | [Dijkstra shortest paths](docs/reference-algorithms.md#dijkstra-shortest-paths) | Finds distances to reachable vertices with nonnegative integer weights. |
| Trees | [Inorder traversal](docs/reference-algorithms.md#inorder-tree-traversal) | Visits a binary tree in left, root, right order using an explicit stack. |
| Heaps | [K largest values](docs/reference-algorithms.md#k-largest-values) | Returns up to k values in descending order, retaining duplicates. |
| Intervals | [Merge intervals](docs/reference-algorithms.md#merge-closed-intervals) | Returns the sorted union of closed intervals. |
| Dynamic programming | [Longest common subsequence length](docs/reference-algorithms.md#longest-common-subsequence-length) | Finds the shared subsequence length using a single row of state. |

## Run tests

The maintained CPython versions are 3.11 through 3.15. [Python's version status](https://devguide.python.org/versions/)

On macOS or Linux, run this from the repository root.

```bash
PYTHONPATH=python python3 -m unittest discover -s tests -v
```

On Windows PowerShell, run these commands from the repository root.

```powershell
$env:PYTHONPATH='python'
py -3 -m unittest discover -s tests -v
```

Set the same `PYTHONPATH` to import the public functions from `algolab`. The tests cover boundary cases, a tree deeper than Python's default recursion limit, and comparisons with independent small-input algorithms. [Test suite](tests/)

The CI workflow runs the suite on each maintained version. [Workflow](.github/workflows/ci.yml) · [Run history](https://github.com/SHUBHRAGHAVT-57/algorithmic-lab/actions/workflows/ci.yml)

## Contributing

Contributions include a clear problem description, complexity analysis, and edge-case tests. See [Contributing](CONTRIBUTING.md), the [roadmap](docs/roadmap.md), and the [changelog](CHANGELOG.md).

## License

Released under the MIT License. [License text](LICENSE)
