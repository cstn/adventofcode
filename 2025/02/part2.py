import advent.parser as ap


def main(filename):
    parsed_line = ap.read_line_input(filename, ',', dtype=str)

    result = 0
    for token in parsed_line:
        id_range = list(map(int, token.split('-')))
        for r in range(id_range[0], id_range[1] + 1):
            s = str(r)

            for i in range(1, len(s) // 2 + 1):
                # only if you can split the string into chunks of the same length
                if len(s) % i == 0:
                    chunks = list(map(''.join, zip(*[iter(s)] * i)))
                    unique_chunks = set(chunks)
                    if len(unique_chunks) == 1:
                        result += r
                        # count only one occurrence
                        break

    return result


print('Part 2')
print('Sample result', main('sample2.txt'))
print('Main result', main('input2.txt'))
