import numpy as np
import advent.parser as ap


class Guard:
    def __init__(self, matrix):
        [[y, x]] = np.argwhere(matrix == '^')
        self.x = x
        self.y = y
        g = matrix[y, x]
        if g == '^':
            self.direction = 'up'
        elif g == '>':
            self.direction = 'right'
        elif g == 'v':
            self.direction = 'down'
        else:
            self.direction = 'left'


    def turn(self):
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'left'
        else:
            self.direction = 'up'

        return self.direction


    def end_position(self, matrix):
        if self.y == 0 and self.direction == 'up':
            return True
        if self.x == 0 and self.direction == 'left':
            return True
        if self.x == len(matrix[0]) - 1 and self.direction == 'right':
            return True
        if self.y == len(matrix) -1 and self.direction == 'down':
            return True
        return False


    def next(self, matrix):
        if self.direction == 'up':
            return matrix[self.y - 1, self.x]
        if self.direction == 'down':
            return matrix[self.y + 1, self.x]
        if self.direction == 'left':
            return matrix[self.y, self.x - 1]
        if self.direction == 'right':
            return matrix[self.y, self.x + 1]


    def move(self, matrix):
        if self.next(matrix) in ('#', 'O'):
            self.turn()

        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1


def main(filename):
    matrix_input = ap.read_matrix_input(filename, None, dtype=str)
    matrix_origin = np.copy(matrix_input)
    max_steps = len(matrix_origin) * len(matrix_origin[0])

    obstacles = 0
    for y in range(len(matrix_origin)):
        for x in range(len(matrix_origin[y])):
            if matrix_origin[y, x] in ('#', '^') or  (y < len(matrix_origin) - 1 and matrix_origin[y + 1, x] == '^'):
                continue

            matrix = np.copy(matrix_origin)
            matrix[y, x] = 'O'
            guard = Guard(matrix)

            step = 0
            while not guard.end_position(matrix) and step < max_steps:
                guard.move(matrix)
                matrix[guard.y, guard.x] = 'X'
                step += 1

            if not guard.end_position(matrix):
                obstacles += 1


    return obstacles


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
