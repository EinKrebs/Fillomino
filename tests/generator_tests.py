import unittest

import generator


class GeneratorTests(unittest.TestCase):
    def test_dfs(self):
        test = [[2, 4, 4, 4, 1],
                [3, 3, 4, 6, 3],
                [6, 6, 6, 6, 6],
                [5, 4, 4, 5, 5],
                [2, 4, 4, 5, 5]]
        self.assertEqual(generator.dfs(0, 4, test, [[False for _ in range(5)]
                                                    for _ in range(5)], 5, 5),
                         1)
        self.assertEqual(generator.dfs(0, 0, test, [[False for _ in range(5)]
                                                    for _ in range(5)], 5, 5),
                         2)
        self.assertEqual(generator.dfs(1, 0, test, [[False for _ in range(5)]
                                                    for _ in range(5)], 5, 5),
                         3)
        self.assertEqual(generator.dfs(0, 1, test, [[False for _ in range(5)]
                                                    for _ in range(5)], 5, 5),
                         8)
        self.assertEqual(generator.dfs(3, 0, test, [[False for _ in range(5)]
                                                    for _ in range(5)], 5, 5),
                         5)
        self.assertEqual(generator.dfs(2, 0, test, [[False for _ in range(5)]
                                                    for _ in range(5)], 5, 5),
                         6)

    def test_is_solution(self):
        test = [[2, 4, 4, 4, 1],
                [3, 3, 4, 6, 3],
                [6, 6, 6, 6, 6],
                [5, 4, 4, 5, 5],
                [2, 4, 4, 5, 5]]
        self.assertTrue(generator.is_solution(test, 5, 5))
        test = [[1, 4, 4, 4, 1],
                [3, 3, 4, 6, 3],
                [6, 6, 6, 6, 6],
                [5, 4, 4, 5, 5],
                [1, 4, 4, 5, 5]]
        self.assertFalse(generator.is_solution(test, 5, 5))
        test = [[3, 4, 4, 4, 1],
                [3, 3, 4, 6, 3],
                [6, 6, 6, 6, 6],
                [5, 4, 4, 5, 5],
                [3, 4, 4, 5, 5]]
        self.assertFalse(generator.is_solution(test, 5, 5))
