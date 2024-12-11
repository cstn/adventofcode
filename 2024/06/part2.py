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
        if self.x == len(matrix[self.y]) - 1 and self.direction == 'right':
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
    size_y, size_x = matrix_input.shape

    matrix_solution = np.copy(matrix_input)
    guard = Guard(matrix_solution)
    start_x, start_y = guard.x, guard.y
    while not guard.end_position(matrix_solution):
        guard.move(matrix_solution)
        matrix_solution[guard.y, guard.x] = 'X'

    distinct_positions = np.argwhere(matrix_solution == 'X')

    max_steps = size_y * size_x

    obstacles = []
    for [y, x] in distinct_positions:
        if x == start_x and y == start_y:
            continue

        matrix = np.copy(matrix_input)
        matrix[y, x] = 'O'
        guard = Guard(matrix)

        step = 0
        while not guard.end_position(matrix) and step < max_steps:
            guard.move(matrix)
            matrix[guard.y, guard.x] = 'X'
            step += 1

        if not guard.end_position(matrix):
            if not [y, x] in obstacles:
                obstacles.append([y, x])

    print('Obstacles', len(obstacles))

    return len(obstacles)


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
