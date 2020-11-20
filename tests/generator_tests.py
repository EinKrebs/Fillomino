import unittest
import random

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

    def test_generate_random(self):
        random.seed(100)
        for _ in range(10):
            puzzle, solution = generator.random_generate(4, 4, 2, 5)
            self.assertEqual(puzzle.width, 4)
            self.assertEqual(puzzle.height, 4)
            self.assertEqual(solution.width, 4)
            self.assertEqual(solution.height, 4)
            count = 0
            arr = [[0 for _ in range(4)] for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    self.assertFalse(solution[i, j].empty)
                    self.assertLessEqual(solution[i, j].value, 5)
                    self.assertGreaterEqual(solution[i, j].value, 2)
                    self.assertTrue(puzzle[i, j].empty
                                    or puzzle[i, j] == solution[i, j])
                    if not puzzle[i, j].empty:
                        count += 1
                    arr[i][j] = solution[i, j].value
            self.assertTrue(generator.is_solution(arr, 4, 4))
            self.assertLess(count, 16 * 0.4)
