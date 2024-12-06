def print_matrix(matrix, separator = ''):
    print('\n'.join(separator.join('{0}'.format(item) for item in row) for row in matrix))
