def print_matrix(matrix):
    print('\n'.join('\t'.join(' {0} '.format(item) for item in row) for row in matrix))
