def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return [line.strip() for line in lines]
