# filename = 'sample2.txt'
filename = 'input.txt'

spelled_digits = dict({
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
})


def spelled(text):
    first_token = 'notfound'
    first_pos = 1000
    last_token = 'notfound'
    last_pos = -1
    for token in list(spelled_digits):
        if -1 < text.find(token) < first_pos:
            first_pos = text.index(token)
            first_token = token
        if -1 < text.find(token) > last_pos:
            last_pos = text.index(token)
            last_token = token

    first_digit = spelled_digits[first_token] if first_token != 'notfound' else ''
    last_digit = spelled_digits[last_token] if last_token != 'notfound' else ''

    return first_digit + text + last_digit


with open(filename, 'r') as f:
    read_data = f.read().splitlines()
f.close()

result = 0
for line in read_data:
    sanitized_line = spelled(line)
    digits = [digit for (index, digit) in enumerate(list(sanitized_line)) if digit.isnumeric()]
    calibration_value = digits[0] + digits[-1]
    result += int(calibration_value)
    print (line, sanitized_line, calibration_value, result)

print(result)
