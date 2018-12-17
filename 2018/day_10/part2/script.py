
class Coord(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector(object):

    def __init__(self, point, velocity):
        self.point = point
        self.velocity = velocity


def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def find_limits(vectors):

    min_x = None
    max_x = None
    min_y = None
    max_y = None

    for v in vectors:
        if min_x is None or v.point.x < min_x:
            min_x = v.point.x
        if min_y is None or v.point.y < min_y:
            min_y = v.point.y
        if max_x is None or v.point.x > max_x:
            max_x = v.point.x
        if max_y is None or v.point.y > max_y:
            max_y = v.point.y

    return min_x, max_x, min_y, max_y

def show(vectors, step):

    if step == 0:
        print('Initially')
    else:
        print('After {} second:'.format(step))

    # find limits
    min_x, max_x, min_y, max_y = find_limits(vectors)
    width = max_x - min_x
    height = max_y - min_y

    if height > 20:
        print (max_y, min_y)
        return

    matrix = [[None for i in range(width + 1)] for i in range(height + 1)]

    aux_vectors = vectors[:]

    for v in aux_vectors:
        x = v.point.x + (-1 * min_x)
        x = int(x * width / (max_x + (-1 * min_x)))
        y = v.point.y + (-1 * min_y)
        y = int(y * height / (max_y + (-1 * min_y)))
        matrix[y][x] = v

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == None:
                print ('.', end='')
            else:
                print ('#', end='')
        print()
    print()

def simulate(vectors):

    for i in range(1000000):

        show(vectors, i)

        for v in vectors:
            v.point.x += v.velocity.x
            v.point.y += v.velocity.y


def extract_vectors(lines):

    vectors = []
    for line in lines:
        position_part, velocity_part = line.split('> velocity=<')

        pos_x, pos_y = position_part.replace('position=<','').split(', ')
        vel_x, vel_y = velocity_part.replace('>', '').split(', ')

        vectors.append(
            Vector(
                Coord(int(pos_x), int(pos_y)),
                Coord(int(vel_x), int(vel_y))
            )
        )

    return vectors


def main():

    vectors = extract_vectors(read_input())
    simulate(vectors)


if __name__ == '__main__':
    main()
