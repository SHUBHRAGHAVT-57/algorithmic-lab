# Algorithmic Lab

A curated, tested collection of data structures, algorithms, competitive programming techniques, and coding exercises in **Python** and **C++17**.

> Correctness first. Each implementation should explain its contract, complexity, and edge cases, and have automated tests.

## Implemented algorithms

| Topic | Algorithm | Python | C++ |
| --- | --- | --- | --- |
| Arrays | Two Sum | Yes | Yes |
| Arrays | Maximum Subarray (Kadane) | Yes | Yes |
| Search | Lower Bound | Yes | Yes |
| Graphs | BFS shortest paths (unweighted) | Yes | Planned |

## Run tests

**Python 3.10+:**

```bash
PYTHONPATH=python python -m unittest discover -s tests -v
```

**C++17 (GCC/Clang):**

```bash
g++ -std=c++17 -Wall -Wextra -Werror -pedantic -Icpp/include cpp/tests/test_algorithms.cpp -o algolab-tests
./algolab-tests
```

On Windows PowerShell, use `$env:PYTHONPATH='python'; py -3 -m unittest discover -s tests -v` for Python. For C++, use a C++17-capable compiler or GitHub Actions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All submissions must include a clear problem description, complexity analysis, edge-case tests, and original work. Avoid uploading proprietary contest statements or copying third-party solutions without permission.

## License

MIT — see [LICENSE](LICENSE).
