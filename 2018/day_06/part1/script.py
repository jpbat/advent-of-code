from collections import namedtuple

Place = namedtuple('Place', ['id', 'distance', 'x', 'y'])

MATRIX_SIZE = 1000
matrix = [[None for i in range(MATRIX_SIZE)] for i in range(MATRIX_SIZE)]


def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def try_fill(id, x, y, distance):

    if not(x >= 0 and x < MATRIX_SIZE and y >= 0 and y < MATRIX_SIZE):
        return None

    if matrix[x][y] == None:
        matrix[x][y] = Place(id=id, distance=distance, x=x, y=y)
        return matrix[x][y]
    elif matrix[x][y].distance == distance and matrix[x][y].id != id:
        matrix[x][y] = Place(id='X', distance=distance, x=x, y=y)


def fill_matrix(place):

    new_places = []

    if matrix[place.x][place.y] == None:
        matrix[place.x][place.y] = Place(id=place.id, distance=place.distance, x=place.x, y=place.y)

    # Up
    p = try_fill(place.id, place.x, place.y + 1, place.distance + 1)
    if p != None:
        new_places.append(p)

    # Down
    p = try_fill(place.id, place.x, place.y - 1, place.distance + 1)
    if p != None:
        new_places.append(p)

    # Left
    p = try_fill(place.id, place.x - 1, place.y, place.distance + 1)
    if p != None:
        new_places.append(p)

    # Right
    p = try_fill(place.id, place.x + 1, place.y, place.distance + 1)
    if p != None:
        new_places.append(p)

    return new_places


def main():

    lines = read_input()

    places = []
    for i in range(len(lines)):
        places.append(
            Place(
                id = i,
                distance = 0,
                x = int(lines[i].split(',')[0]),
                y = int(lines[i].split(' ')[1]),
            )
        )

    while len(places) > 0:

        new_places = []

        for place in places:
            new_places.extend(fill_matrix(place))

        places = new_places

    edges = []
    for i in range(MATRIX_SIZE):
        if matrix[0][i].id not in edges:
            edges.append(matrix[0][i].id)
        if matrix[i][0].id not in edges:
            edges.append(matrix[i][0].id)
        if matrix[MATRIX_SIZE - 1][i].id not in edges:
            edges.append(matrix[MATRIX_SIZE - 1][i].id)
        if matrix[i][MATRIX_SIZE - 1].id not in edges:
            edges.append(matrix[i][MATRIX_SIZE - 1].id)

    counter = {}
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):

            if matrix[i][j].id in edges:
                continue

            if matrix[i][j].id not in counter:
                counter[matrix[i][j].id] = 0

            counter[matrix[i][j].id] += 1

    max_v = None
    for k, v in counter.items():
        if max_v is None or counter[k] > max_v:
            max_v = counter[k]

    print (max_v)


if __name__ == '__main__':
    main()
