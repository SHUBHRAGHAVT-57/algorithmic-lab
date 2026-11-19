"""Contract examples and independent small-input oracles for reference algorithms."""
import itertools
import random
import unittest

import algolab


class ReferenceAlgorithmsTest(unittest.TestCase):
    def require(self, name):
        implementation = getattr(algolab, name, None)
        self.assertTrue(callable(implementation), f"{name} is not implemented")
        return implementation

    def test_inorder_empty_and_singleton(self):
        traverse = self.require("inorder_values")
        node = self.require("TreeNode")
        self.assertEqual(traverse(None), [])
        self.assertEqual(traverse(node(-7)), [-7])

    def test_inorder_visits_both_subtrees_without_mutation(self):
        traverse = self.require("inorder_values")
        node = self.require("TreeNode")
        left, middle, right = node(1), node(3), node(4, None, node(5))
        right.left = middle
        root = node(2, left, right)
        self.assertEqual(traverse(root), [1, 2, 3, 4, 5])
        self.assertIs(root.left, left)
        self.assertIs(root.right, right)
        self.assertIs(right.left, middle)

    def test_inorder_handles_a_tree_deeper_than_python_recursion_limit(self):
        traverse = self.require("inorder_values")
        node = self.require("TreeNode")
        root = tail = node(0)
        for value in range(1, 2000):
            tail.right = node(value)
            tail = tail.right
        self.assertEqual(traverse(root), list(range(2000)))

    def test_k_largest_preserves_duplicates_and_handles_boundaries(self):
        largest = self.require("k_largest")
        self.assertEqual(largest([4, -1, 4, 2], 3), [4, 4, 2])
        self.assertEqual(largest([2, -3], 8), [2, -3])
        self.assertEqual(largest([], 2), [])
        self.assertEqual(largest([5], 0), [])

    def test_k_largest_rejects_negative_and_noninteger_counts(self):
        largest = self.require("k_largest")
        with self.assertRaises(ValueError):
            largest([1], -1)
        for invalid in (1.5, "2", None, True):
            with self.subTest(k=invalid), self.assertRaises(TypeError):
                largest([1], invalid)

    def test_k_largest_matches_sorting_oracle_for_single_pass_inputs(self):
        largest = self.require("k_largest")
        rng = random.Random(1901)
        for _ in range(200):
            values = [rng.randrange(-9, 10) for _ in range(rng.randrange(40))]
            before = values.copy()
            k = rng.randrange(len(values) + 5)
            with self.subTest(values=values, k=k):
                self.assertEqual(largest(iter(values), k), sorted(before, reverse=True)[:k])
                self.assertEqual(values, before)

    def test_dijkstra_improves_prior_routes_and_handles_zero_weight_cycles(self):
        shortest = self.require("dijkstra_shortest_paths")
        graph = {0: [(1, 9), (2, 1), (1, 8)], 2: [(1, 2)], 1: [(3, 0)], 3: [(1, 0)], 99: []}
        before = {node: edges.copy() for node, edges in graph.items()}
        self.assertEqual(shortest(graph, 0), {0: 0, 1: 3, 2: 1, 3: 3})
        self.assertEqual(graph, before)

    def test_dijkstra_includes_source_and_neighbor_only_vertices(self):
        shortest = self.require("dijkstra_shortest_paths")
        self.assertEqual(shortest({}, 7), {7: 0})
        self.assertEqual(shortest({-2: [(5, 0)]}, -2), {-2: 0, 5: 0})
        weight = 2 ** 100
        self.assertEqual(shortest({0: [(1, weight)], 1: [(2, weight)]}, 0), {0: 0, 1: weight, 2: 2 * weight})

    def test_dijkstra_rejects_negative_weights_even_outside_the_reachable_component(self):
        shortest = self.require("dijkstra_shortest_paths")
        for graph in ({0: [(1, -1)]}, {99: [(100, -1)]}):
            with self.subTest(graph=graph), self.assertRaises(ValueError):
                shortest(graph, 0)

    def test_dijkstra_rejects_noninteger_weights(self):
        shortest = self.require("dijkstra_shortest_paths")
        for weight in (1.5, float("inf"), float("nan"), True, "3"):
            with self.subTest(weight=weight), self.assertRaises(TypeError):
                shortest({0: [(1, weight)]}, 0)

    def test_dijkstra_matches_bellman_ford_oracle_on_small_graphs(self):
        shortest = self.require("dijkstra_shortest_paths")
        rng = random.Random(1902)
        for _ in range(100):
            count = rng.randrange(1, 7)
            graph = {node: [(other, rng.randrange(8)) for other in range(count) if rng.random() < 0.3]
                     for node in range(count)}
            source = rng.randrange(count)
            expected = {source: 0}
            for _ in range(count - 1):
                for node, edges in graph.items():
                    if node in expected:
                        for other, weight in edges:
                            distance = expected[node] + weight
                            if distance < expected.get(other, float("inf")):
                                expected[other] = distance
            with self.subTest(graph=graph, source=source):
                self.assertEqual(shortest(graph, source), expected)

    def test_interval_merge_handles_unsorted_nested_touching_and_point_intervals(self):
        merge = self.require("merge_intervals")
        intervals = [(5, 7), (1, 3), (2, 6), (7, 8), (10, 10), (12, 13), (2, 2)]
        before = intervals.copy()
        self.assertEqual(merge(intervals), [(1, 8), (10, 10), (12, 13)])
        self.assertEqual(intervals, before)

    def test_interval_merge_accepts_empty_and_single_pass_inputs(self):
        merge = self.require("merge_intervals")
        self.assertEqual(merge([]), [])
        self.assertEqual(merge(iter([(3, 3), (-2, -1), (0, 1)])), [(-2, -1), (0, 1), (3, 3)])

    def test_interval_merge_rejects_reversed_endpoints(self):
        merge = self.require("merge_intervals")
        with self.assertRaises(ValueError):
            merge([(0, 1), (8, 3)])

    def test_interval_merge_matches_independently_enumerated_union(self):
        merge = self.require("merge_intervals")
        rng = random.Random(1903)
        for _ in range(150):
            intervals = [tuple(sorted((rng.randrange(-4, 5), rng.randrange(-4, 5))))
                         for _ in range(rng.randrange(10))]
            # Half-unit samples distinguish a genuine gap from touching closed intervals.
            points = sorted({point for start, end in intervals for point in range(2 * start, 2 * end + 1)})
            components = []
            for point in points:
                if components and point == components[-1][1] + 1:
                    components[-1][1] = point
                else:
                    components.append([point, point])
            expected = [(start // 2, end // 2) for start, end in components]
            with self.subTest(intervals=intervals):
                self.assertEqual(merge(intervals), expected)

    def test_lcs_handles_empty_repeated_and_noncontiguous_matches(self):
        length = self.require("longest_common_subsequence_length")
        for left, right, expected in [("", "abc", 0), ("abc", "", 0), ("abcde", "ace", 3),
                                      ("aaaa", "aa", 2), ("abc", "cba", 1), ("abc", "xyz", 0)]:
            with self.subTest(left=left, right=right):
                self.assertEqual(length(left, right), expected)

    def test_lcs_uses_unicode_codepoints_without_normalization(self):
        length = self.require("longest_common_subsequence_length")
        self.assertEqual(length("😀a😀", "😀😀"), 2)
        self.assertEqual(length("é", "e\u0301"), 0)
        self.assertEqual(length("a" * 10000, "a"), 1)

    def test_lcs_matches_exhaustive_subsequence_oracle(self):
        length = self.require("longest_common_subsequence_length")
        rng = random.Random(1904)
        for _ in range(150):
            left = "".join(rng.choice("abç") for _ in range(rng.randrange(8)))
            right = "".join(rng.choice("abç") for _ in range(rng.randrange(8)))
            expected = 0
            for size in range(1, len(left) + 1):
                for positions in itertools.combinations(range(len(left)), size):
                    remaining = iter(right)
                    if all(left[index] in remaining for index in positions):
                        expected = size
                        break
            with self.subTest(left=left, right=right):
                self.assertEqual(length(left, right), expected)
                self.assertEqual(length(right, left), expected)


if __name__ == "__main__":
    unittest.main()

