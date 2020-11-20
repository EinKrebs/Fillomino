import unittest
import random

from domain.entry import Entry


class EntryTests(unittest.TestCase):
    def test_init_int(self):
        random.seed(100)
        for _ in range(10000):
            number = random.randint(-1000, 1000)
            if number <= 0:
                self.assertRaises(ValueError, lambda: Entry(number))
            else:
                entry = Entry(number)
                self.assertFalse(entry.empty)
                self.assertEqual(entry.value, number)

    def test_init_str(self):
        entry = Entry('.')
        self.assertTrue(entry.empty)
        incorrect = ['alsdkhj', '', ' ', '|', '_']
        for case in incorrect:
            self.assertRaises(ValueError, lambda: Entry(case))

    def test_incorrect_class(self):
        self.assertRaises(TypeError, lambda: Entry(1.1))
        self.assertRaises(TypeError, lambda: Entry(b'.'))
        self.assertRaises(TypeError, lambda: Entry(['.']))
        self.assertRaises(TypeError, lambda: Entry({'.'}))

    def test_get_empty(self):
        self.assertTrue(Entry.get_empty().empty)

    def test_str(self):
        self.assertEqual(str(Entry.get_empty()), '.')
        random.seed(100)
        for i in range(10000):
            number = random.randint(1, 1000)
            self.assertEqual(str(Entry(number)), str(number))

    def test_eq(self):
        empty = Entry.get_empty()
        self.assertEqual(empty, Entry('.'))
        random.seed(100)
        for i in range(10000):
            first = random.randint(1, 1000)
            self.assertEqual(Entry(first), Entry(first))
            self.assertEqual(Entry(first), first)
            second = random.randint(first + 1, 1100)
            self.assertNotEqual(Entry(first), Entry(second))
            self.assertNotEqual(Entry(first), second)
        for i in range(10000):
            number = random.randint(1, 1000)
            self.assertNotEqual(Entry(number),
                                random.random() % 3.1415926)
            self.assertNotEqual(Entry(number),
                                [number])
