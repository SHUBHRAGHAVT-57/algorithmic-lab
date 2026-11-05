# Algorithmic Lab

A curated, tested collection of data structures, algorithms, competitive programming techniques, and coding exercises in **Python 3**.

Maintained by [Shubh Raghav](https://github.com/SHUBHRAGHAVT-57).

**Current scope:** four Python implementations. C++ solutions and additional topics are future work; see [the roadmap](docs/roadmap.md).

> Correctness first. Each implementation should explain its contract, complexity, and edge cases, and have automated tests.

## Implemented algorithms

| Topic | Implementation | Contract |
| --- | --- | --- |
| Arrays | [Two Sum](python/algolab/arrays.py) | Distinct matching indices, or `None`; O(n) time and space |
| Arrays | [Maximum Subarray](python/algolab/arrays.py) | Largest nonempty contiguous sum; rejects empty input; O(n) time |
| Search | [Lower Bound](python/algolab/search.py) | First insertion position in ascending sorted input; O(log n) time |
| Graphs | [BFS shortest paths](python/algolab/graphs.py) | Hop distances to reachable nodes in an unweighted directed graph; O(V + E) time |

## Run tests

Requires Python 3.10+.

On macOS or Linux:

```bash
PYTHONPATH=python python -m unittest discover -s tests -v
```

On Windows PowerShell:

```powershell
$env:PYTHONPATH='python'
py -3 -m unittest discover -s tests -v
```

The package exports these functions from `python/algolab/__init__.py`. The [test suite](tests/test_algorithms.py) exercises duplicate values, empty inputs, negative arrays and shortest-hop graph traversal. [Python CI](.github/workflows/ci.yml) runs the suite; check its latest run for the current result.

## Daily LeetCode practice

Solve a problem yourself, submit it on LeetCode, then add your own accepted Python solution with its approach, time/space complexity, and edge-case tests. Start with Easy problems and gradually introduce Medium problems.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All submissions must include a clear problem description, complexity analysis, edge-case tests, and original work. Avoid uploading proprietary contest statements or copying third-party solutions without permission.

## License

MIT — see [LICENSE](LICENSE).
