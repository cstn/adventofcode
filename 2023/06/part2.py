
def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def calc_speed(button_down_time):
    return button_down_time


def calc_distance(total_time, button_down_time, speed):
    return (total_time - button_down_time) * speed


def main(filename):
    read_lines = read_input(filename)
    sanitized_lines = [line.replace(' ', '').replace('Time:', '').replace('Distance:', '') for line in read_lines]
    races = list(map(lambda x: [int(x)], sanitized_lines))
    print(races)

    ways_to_win = 1
    for i, time in enumerate(races[0]):
        print('Time', time)
        button_down_times = range(0, time + 1)
        wins = []
        for button_down_time in button_down_times:
            speed = calc_speed(button_down_time)
            distance = calc_distance(time, button_down_time, speed)
            if distance > races[1][i]:
                wins.append(button_down_time)
        print('Wins', wins)
        ways_to_win *= len(wins)
    return ways_to_win


# filename = 'sample.txt'
filename = 'input.txt'
print('Result', main(filename))
