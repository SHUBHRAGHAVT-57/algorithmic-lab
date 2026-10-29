# Algorithmic Lab

A curated, tested collection of data structures, algorithms, competitive programming techniques, and coding exercises in **Python 3**.

> Correctness first. Each implementation should explain its contract, complexity, and edge cases, and have automated tests.

## Implemented algorithms

| Topic | Algorithm | Python |
| --- | --- | --- |
| Arrays | Two Sum | Yes |
| Arrays | Maximum Subarray (Kadane) | Yes |
| Search | Lower Bound | Yes |
| Graphs | BFS shortest paths (unweighted) | Yes |

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

## Daily LeetCode practice

Solve a problem yourself, submit it on LeetCode, then add your own accepted Python solution with its approach, time/space complexity, and edge-case tests. Start with Easy problems and gradually introduce Medium problems.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All submissions must include a clear problem description, complexity analysis, edge-case tests, and original work. Avoid uploading proprietary contest statements or copying third-party solutions without permission.

## License

MIT — see [LICENSE](LICENSE).
