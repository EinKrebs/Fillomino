import typing

from domain.entry import Entry


def check_index(i, list_size):
    return 0 <= i < list_size


class Puzzle:
    def __init__(self,
                 content: typing.List[
                     typing.List[typing.Union[int, Entry]]]):
        self.height = len(content)
        if self.height == 0:
            self.width = 0
            return
        self.width = len(content[0])
        self.content = content
        for line in self.content:
            if len(line) != self.width:
                raise ValueError("Line lengths differ")
            for i in range(self.width):
                elem = line[i]
                if isinstance(elem, int):
                    line[i] = Entry(elem)
                elif not isinstance(elem, Entry):
                    raise TypeError("Only int or Entry types are supported")

    def __getitem__(self, item: typing.Tuple[int, int]):
        i, j = item
        if not check_index(i, self.height):
            raise ValueError("Invalid height")
        if not check_index(j, self.width):
            raise ValueError("Invalid width")
        return self.content[i][j]

    def __str__(self):
        return (f'{self.width} {self.height}\n'
                + '\n'.join((' '.join(str(entry) for entry in line))
                            for line in self.content))

    @staticmethod
    def from_str(text):
        lines = text.split('\n')
        width, height = map(int, lines[0].split())
        if len(lines) != height + 1:
            raise ValueError("Incorrect input height")
        content = [list(map(Entry, line.split())) for line in lines[1:]]
        puzzle = Puzzle(content)
        if puzzle.width != width:
            raise ValueError("Incorrect input width")
        return puzzle
