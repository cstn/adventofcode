import advent.parser as ap

def main(filename):
    parsed_line = ap.read_line_input(filename, ',', dtype=str)

    result = 0
    for token in parsed_line:
        id_range = list(map(int, token.split('-')))
        for r in range(id_range[0], id_range[1]+1):
            s = str(r)
            if len(s) % 2 == 0:
                if s[0:len(s) // 2] == s[len(s) // 2:]:
                    result += r

    return result


print('Part 1')
print('Sample result', main('sample1.txt'))
print('Main result', main('input1.txt'))
