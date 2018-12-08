from collections import namedtuple

Place = namedtuple('Place', ['x', 'y'])

FRINGE_SIZE = 10000

fringe = {}


def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def fill_grid(place):

    for fringe_key, fringe_item in fringe.items():
        if fringe[fringe_key]['distance'] >= FRINGE_SIZE:
            continue
        fringe[fringe_key]['distance'] += abs(fringe_item['x'] - place.x) + abs(fringe_item['y'] - place.y)


def main():

    lines = read_input()

    places = []
    for i in range(len(lines)):
        places.append(
            Place(
                x = int(lines[i].split(',')[0]),
                y = int(lines[i].split(' ')[1]),
            )
        )

    center = places[0]
    for i in range(400):
        for j in range(400):

            if i + j >= FRINGE_SIZE:
                continue

            key = '{}.{}'.format(center.x + i, center.y + j)
            fringe[key] = {
                'distance': abs(center.x + i - center.x) + abs(center.y + j - center.y),
                'x': center.x + i,
                'y': center.y + j
            }

            key = '{}.{}'.format(center.x + i, center.y - j)
            fringe[key] = {
                'distance': abs(center.x + i - center.x) + abs(center.y - j - center.y),
                'x': center.x + i,
                'y': center.y - j
            }

            key = '{}.{}'.format(center.x - i, center.y + j)
            fringe[key] = {
                'distance': abs(center.x - i - center.x) + abs(center.y + j - center.y),
                'x': center.x - i,
                'y': center.y + j
            }

            key = '{}.{}'.format(center.x - i, center.y - j)
            fringe[key] = {
                'distance': abs(center.x - i - center.x) + abs(center.y - j - center.y),
                'x': center.x - i,
                'y': center.y - j
            }

    for place in places[1:]:
        fill_grid(place)

    counter = 0
    for k, v in fringe.items():
        if v['distance'] < FRINGE_SIZE:
            counter += 1
    print (counter)


if __name__ == '__main__':
    main()
