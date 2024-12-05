from advent.files import read_input

def is_correct_order(page_update, page_ordering_rules):
    for i in range(len(page_update) - 1):
        for j in range(i + 1, len(page_update)):
            violated_rules = [r for r in page_ordering_rules if r == [page_update[j], page_update[i]]]
            if len(violated_rules) > 0:
                return False

    return True


def reorder(page_update, page_ordering_rules):
    for i in range(len(page_update) - 1):
        for j in range(i + 1, len(page_update)):
            for r in page_ordering_rules:
                if r == [page_update[j], page_update[i]]:
                    page_update[i], page_update[j] = page_update[j], page_update[i]

    return page_update


def main(filename):
    lines = read_input(filename)
    page_ordering_rules = [list(map(int, l.split('|'))) for l in lines if l.find('|') > 0]
    page_updates = [list(map(int, l.split(','))) for l in lines if l.find(',') > 0]

    result = 0
    for page_update in page_updates:
        if not is_correct_order(page_update, page_ordering_rules):
            correct_page_update = reorder(page_update, page_ordering_rules)
            middle = correct_page_update[len(correct_page_update) // 2]
            result += middle

    return result


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
