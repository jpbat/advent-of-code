def extract_coords(line):

    _, _, coords, dimension  = line.replace(':','').split()
    top_left_x, top_left_y = coords.split(',')
    dimension_x, dimension_y = dimension.split('x')
    top_left_x = int(top_left_x)
    top_left_y = int(top_left_y)
    bot_right_x = top_left_x + int(dimension_x)
    bot_right_y = top_left_y + int(dimension_y)
    return (
        (top_left_x, top_left_y),
        (bot_right_x, bot_right_y),
    )


def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def main():

    indexes = {}
    lines = read_input()

    for line in lines:
        top_left, bottom_right = extract_coords(line)

        for i in range(top_left[0], bottom_right[0]):
            for j in range(top_left[1], bottom_right[1]):
                key = '{}.{}'.format(i, j)
                if key not in indexes:
                    indexes[key] = 0
                indexes[key] += 1

    counter = 0
    for k, v in indexes.items():
        if v >= 2:
            counter += 1

    print (counter)

if __name__ == '__main__':
    main()
