def read_input(name, strip=False):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    if strip:
        return [line.strip() for line in lines]
    else:
        return lines
