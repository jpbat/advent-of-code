
GRID_SIDE = 300


def get_cell_power_level(x, y, grid_serial_number):

    rackID = x + 10
    power_lvl = rackID * y
    power_lvl += grid_serial_number
    power_lvl *= rackID
    try:
        power_lvl = int(str(power_lvl)[-3])
    except Exception:
        power_lvl = 0
    power_lvl -= 5
    return power_lvl


def get_power_square(x, y, grid):
    power = 0
    for i in range(3):
        for j in range(3):
            power += grid[x + i][y + j]
    return power


def main():

    grid_serial_number = int(input())

    grid = []
    for x in range(GRID_SIDE):
        line = []
        for y in range(GRID_SIDE):
            line.append(get_cell_power_level(x + 1, y + 1, grid_serial_number))
        grid.append(line)

    max_power = (None, 0)
    for x in range(GRID_SIDE - 3):
        for y in range(GRID_SIDE - 3):
            power = get_power_square(x, y, grid)
            if max_power[0] is None or max_power[1] < power:
                max_power = ((x, y), power)

    print ('{},{}'.format(max_power[0][0] + 1, max_power[0][1] + 1))


if __name__ == '__main__':
    main()
