import numpy as np
import re

filename = 'sample.txt'
# filename = 'input.txt'

with open(filename, 'r') as f:
    read_data = list(map(lambda x: re.split(': |\s+', x), f.read().splitlines()))
f.close()


def main():
    return 0


print('Result', main())
