# filename = 'sample1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    read_data = f.read().splitlines()
f.close()

result = 0
for line in read_data:
    digits = [digit for (index, digit) in enumerate(list(line)) if digit.isnumeric()]
    calibration_value = digits[0] + digits[-1]
    result += int(calibration_value)

print(result)
