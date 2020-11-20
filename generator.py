import typing
import random
import copy

from domain.entry import Entry
from domain.puzzle import Puzzle


deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def random_generate(width, height, min_value, max_value)\
        -> typing.Tuple[Puzzle, Puzzle]:
    if min_value <= 0 or max_value <= 0 or min_value <= max_value:
        raise ValueError("Invalid min/max value")
    while True:
        res = [[random.randint(min_value, max_value) for _ in range(width)]
               for _ in range(height)]
        completed = copy.deepcopy(res)
        if is_solution(res, width, height):
            count = width * height
            while count > 0.4 * width * height:
                i = random.randint(0, height - 1)
                j = random.randint(0, width - 1)
                if res[i][j] != '.':
                    count -= 1
                    res[i][j] = '.'
            return (Puzzle([list(map(Entry, line)) for line in res]),
                    Puzzle([list(map(Entry, line)) for line in completed]))


def is_solution(arr, width, height):
    visited = [[False for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if not visited[i][j]:
                count = dfs(i, j, arr, visited, width, height)
                if count % arr[i][j] != 0 or (arr[i][j] == 1 and count != 1):
                    return False
    return True


def dfs(i, j, arr, visited, width, height):
    count = 1
    visited[i][j] = True
    for delta_y, delta_x in deltas:
        y = (i + delta_y + height) % height
        x = (j + delta_x + width) % width
        if arr[y][x] == arr[i][j] and not visited[y][x]:
            count += dfs(y, x, arr, visited, width, height)
    return count
