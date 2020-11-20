import typing

from domain.entry import Entry


def check_index(i, list_size):
    return 0 <= i < list_size


class Puzzle:
    def __init__(self,
                 content: typing.List[
                     typing.List[Entry]]):
        self.content = content
        self.height = len(content)
        if self.height == 0:
            self.width = 0
            return
        self.width = len(content[0])
        for line in content:
            if len(line) != self.width:
                raise ValueError("Line lengths differ")

    def __getitem__(self, item: typing.Tuple[int, int]):
        i, j = item
        if not check_index(i, self.height):
            raise ValueError("Invalid height")
        if not check_index(j, self.width):
            raise ValueError("Invalid width")
        return self.content[i][j]

    def to_str(self):
        return '\n'.join((' '.join(str(entry) for entry in line))
                         for line in self.content)

    @staticmethod
    def from_str(text):
        lines = text.split('\n')
        width, height = lines[0].spilt()
        if len(lines) == height - 1:
            raise ValueError("Incorrect input height")
        content = [list(map(Entry, line.split())) for line in lines]
        puzzle = Puzzle(content)
        if puzzle.width != width:
            raise ValueError("Incorrect input width")
