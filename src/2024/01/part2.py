import advent.parser as ap

def similarity_score(matrix):
    result = 0
    for i in range(len(matrix[0])):
        count = 0
        for j in range(len(matrix[1])):
            if matrix[1, j] == matrix[0, i]:
                count += 1
        result += matrix[0, i] * count

    return result


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '\s+', dtype=int)
    transposed_lines = parsed_lines.transpose()

    return similarity_score(transposed_lines)


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
