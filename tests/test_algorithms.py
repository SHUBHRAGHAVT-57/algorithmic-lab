import unittest
from algolab import two_sum, maximum_subarray, lower_bound, bfs_shortest_paths

class AlgorithmsTest(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(two_sum([3, 3], 6), (0, 1))
        self.assertIsNone(two_sum([1, 2], 8))
        self.assertIsNone(two_sum([], 0))

    def test_maximum_subarray(self):
        self.assertEqual(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maximum_subarray([-5, -1, -9]), -1)
        with self.assertRaises(ValueError):
            maximum_subarray([])

    def test_lower_bound(self):
        self.assertEqual(lower_bound([1, 2, 2, 4], 2), 1)
        self.assertEqual(lower_bound([1, 2, 2, 4], 3), 3)
        self.assertEqual(lower_bound([], 5), 0)

    def test_bfs(self):
        self.assertEqual(bfs_shortest_paths({1: [2, 3], 2: [4], 3: [4]}, 1), {1: 0, 2: 1, 3: 1, 4: 2})
        self.assertEqual(bfs_shortest_paths({}, 7), {7: 0})

if __name__ == '__main__':
    unittest.main()
