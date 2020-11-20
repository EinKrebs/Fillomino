import unittest
import random

from domain.puzzle import Puzzle
from domain.entry import Entry


class PuzzleTests(unittest.TestCase):
    def test_init_incorrect_width(self):
        arr = [[Entry(1), Entry(1), Entry(1)],
               [Entry(1), 1],
               [Entry(1), Entry(1), Entry(1)]]
        self.assertRaises(ValueError, lambda: Puzzle(arr))

    def test_init_incorrect_types(self):
        arr = [['a', 1, 1],
               [1, 1, 1]]
        self.assertRaises(TypeError, lambda: Puzzle(arr))
        arr = [[1, 1, 1],
               [1, 1, 1.1]]
        self.assertRaises(TypeError, lambda: Puzzle(arr))

    def test_int_elements(self):
        random.seed(100)
        width = random.randint(4, 10)
        height = random.randint(4, 10)
        arr = [[Entry(random.randint(1, 10)
                      if random.randint(0, 1) == 1
                      else '.')
                if random.randint(0, 1) == 1
                else random.randint(1, 10)
                for _ in range(width)] for _ in range(height)]
        puzzle = Puzzle(arr)
        for i in range(height):
            for j in range(width):
                orig = arr[i][j]
                puz = puzzle[i, j]
                self.assertTrue(isinstance(puz, Entry))
                self.assertEqual(puz, orig)

    def test_str_correct(self):
        test = '''5 4
. . 2 . .
. 4 . 2 .
4 . . . 3
. 1 . 3 .'''
        expected = [[Entry.get_empty(), Entry.get_empty(), Entry(2),
                     Entry.get_empty(), Entry.get_empty()],
                    [Entry.get_empty(), Entry(4), Entry.get_empty(),
                     Entry(2), Entry.get_empty()],
                    [Entry(4), Entry.get_empty(), Entry.get_empty(),
                     Entry.get_empty(), Entry(3)],
                    [Entry.get_empty(), Entry(1), Entry.get_empty(),
                     Entry(3), Entry.get_empty()]]
        puzzle = Puzzle.from_str(test)
        self.assertEqual(puzzle.width, 5)
        self.assertEqual(puzzle.height, 4)
        for i in range(4):
            for j in range(5):
                self.assertEqual(expected[i][j], puzzle[i, j])
        self.assertEqual(str(puzzle), test)

    def test_from_str_incorrect_size(self):
        test = '''5 5
. . 2 . .
. 4 . 2 .
4 . . . 3
. 1 . 3 .'''
        self.assertRaises(ValueError, lambda: Puzzle.from_str(test))
        test = '''6 4
. . 2 . .
. 4 . 2 .
4 . . . 3
. 1 . 3 .'''
        self.assertRaises(ValueError, lambda: Puzzle.from_str(test))
        test = '''3 4
. . 2 . .
. 4 . 2 .
4 . . . 3
. 1 . 3 .'''
        self.assertRaises(ValueError, lambda: Puzzle.from_str(test))
