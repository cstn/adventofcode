from advent.files import read_input

def is_correct_order(page_update, page_ordering_rules):
    for i in range(len(page_update) - 1):
        for j in range(i + 1, len(page_update)):
            violated_rules = [r for r in page_ordering_rules if r == [page_update[j], page_update[i]]]
            if len(violated_rules) > 0:
                return False

    return True


def main(filename):
    lines = read_input(filename)
    page_ordering_rules = [list(map(int, l.split('|'))) for l in lines if l.find('|') > 0]
    page_updates = [list(map(int, l.split(','))) for l in lines if l.find(',') > 0]

    result = 0
    for page_update in page_updates:
        if is_correct_order(page_update, page_ordering_rules):
            middle = page_update[len(page_update) // 2]
            result += middle

    return result


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
