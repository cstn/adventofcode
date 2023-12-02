# filename = 'sample2.txt'
filename = 'input.txt'


def first_digit(text):
    if len(text) == 0:
        return ''
    if text[:1].isdigit():
        return text[:1]
    if text.startswith('one'):
        return '1'
    if text.startswith('two'):
        return '2'
    if text.startswith('three'):
        return '3'
    if text.startswith('four'):
        return '4'
    if text.startswith('five'):
        return '5'
    if text.startswith('six'):
        return '6'
    if text.startswith('seven'):
        return '7'
    if text.startswith('eight'):
        return '8'
    if text.startswith('nine'):
        return '9'
    return first_digit(text[1:])


def last_digit(text):
    if len(text) == 0:
        return ''
    if text[-1:].isdigit():
        return text[-1:]
    if text.endswith('one'):
        return '1'
    if text.endswith('two'):
        return '2'
    if text.endswith('three'):
        return '3'
    if text.endswith('four'):
        return '4'
    if text.endswith('five'):
        return '5'
    if text.endswith('six'):
        return '6'
    if text.endswith('seven'):
        return '7'
    if text.endswith('eight'):
        return '8'
    if text.endswith('nine'):
        return '9'
    return last_digit(text[0:-1])


with open(filename, 'r') as f:
    read_data = f.read().splitlines()
f.close()

result = 0

for line in read_data:
    first = first_digit(line)
    last = last_digit(line)
    calibration_value = first + last
    print(calibration_value)
    result += int(calibration_value)

print('Result', result)
