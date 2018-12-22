import time


class Cart(object):

    def __init__(self, id, x, y, char):
        self.id = id
        self.x = x
        self.y = y
        self.char = char
        self.last_turn = None

    def __repr__(self):
        return "[{}, {}] {}".format(self.x, self.y, self.char)


def read_input():

    lines = []
    while True:
        try:
            lines.append(input().replace('\r',''))
        except EOFError:
            break
    return lines


def get_carts(input_data):

    cart_id = 0
    carts = []
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            if input_data[i][j] in ['>', '<', '^', 'v']:
                carts.append(Cart(cart_id, j, i, input_data[i][j]))
                cart_id += 1
    return carts


# def show(grid):
    for y in range(len(grid)):
        print (''.join([c[-1] for c in grid[y]]))
    print()


def reset_char(grid, x, y):

    up_chars = ['|', '\\', '/', '+', '<', '>', '^', 'v']
    down_chars = ['|', '\\', '/', '+', '<', '>', '^', 'v']
    left_chars = ['-', '\\', '/', '+', '<', '>', '^', 'v']
    right_chars = ['-', '\\', '/', '+', '<', '>', '^', 'v']

    # L, R, U, D
    acessible = [0, 0, 0, 0]
    if x > 0 and grid[y][x - 1] in left_chars:
        acessible[0] = 1
    if x < (len(grid[y]) - 1) and grid[y][x + 1] in right_chars:
        acessible[1] = 1
    if y > 0 and grid[y - 1][x] in up_chars:
        acessible[2] = 1
    if y < (len(grid[y]) - 1) and grid[y + 1][x] in down_chars:
        acessible[3] = 1

    if sum(acessible) == 4:
        return '+'

    if sum(acessible) == 3:
        if acessible == [1, 1, 1, 0] or acessible == [1, 1, 0, 1]:
            return '-'
        return '|'

    if acessible == [1, 1, 0, 0]:
        return '-'
    if acessible == [0, 0, 1, 1]:
        return '|'
    if acessible == [1, 0, 0, 1] or acessible == [0, 1, 1, 0]:
        return '\\'
    if acessible == [1, 0, 1, 0] or acessible == [0, 1, 0, 1]:
        return '/'


def next_turn(cart):

    if cart.last_turn == None or cart.last_turn == 'right':
        cart.last_turn = 'left'
        if cart.char == '>':
            return '^'
        if cart.char == '<':
            return 'v'
        if cart.char == '^':
            return '<'
        if cart.char == 'v':
            return '>'

    if cart.last_turn == 'left':
        cart.last_turn = 'straight'
        return cart.char

    if cart.last_turn == 'straight':
        cart.last_turn = 'right'
        if cart.char == '>':
            return 'v'
        if cart.char == '<':
            return '^'
        if cart.char == '^':
            return '>'
        if cart.char == 'v':
            return '<'


def move_cart(grid, cart):

    # exclude cart from current position
    grid[cart.y][cart.x] = grid[cart.y][cart.x][0]

    # move 1 step
    if cart.char == '>':
        cart.x += 1
    elif cart.char == '<':
        cart.x -= 1
    elif cart.char == '^':
        cart.y -= 1
    elif cart.char == 'v':
        cart.y += 1

    # check collision
    if len(grid[cart.y][cart.x]) == 2:
        grid[cart.y][cart.x] = grid[cart.y][cart.x][0]
        return cart.x, cart.y

    # check turns and interceptions
    if grid[cart.y][cart.x] == '+':
        cart.char = next_turn(cart)
    elif cart.char == '>':
        if grid[cart.y][cart.x] == '\\':
            cart.char = 'v'
        elif grid[cart.y][cart.x] == '/':
            cart.char = '^'
    elif cart.char == '<':
        if grid[cart.y][cart.x] == '\\':
            cart.char = '^'
        elif grid[cart.y][cart.x] == '/':
            cart.char = 'v'
    elif cart.char == '^':
        if grid[cart.y][cart.x] == '\\':
            cart.char = '<'
        elif grid[cart.y][cart.x] == '/':
            cart.char = '>'
    else:
        if grid[cart.y][cart.x] == '\\':
            cart.char = '>'
        elif grid[cart.y][cart.x] == '/':
            cart.char = '<'

    # set char to new position
    grid[cart.y][cart.x] += cart.char


def do_cart_cleanup(carts, crash_position, grid):

    crashed = []
    for cart in carts:
        if cart.x == crash_position[0] and cart.y == crash_position[1]:
            crashed.append(cart.id)
    return crashed


def simulate(grid, carts):

    ticks = 0
    while True:

        print (ticks, len(carts))

        # sort carts from top to bottom left to right
        carts.sort(key=lambda c: (c.y, c.x))

        crashed_carts = []
        for cart in carts:
            if cart.id not in crashed_carts:
                crash_position = move_cart(grid, cart)
            if crash_position != None:
                crashed_carts += do_cart_cleanup(carts, crash_position, grid)

        new_carts = []
        for cart in carts:
            if cart.id not in crashed_carts:
                new_carts.append(cart)
        carts = new_carts

        if len(carts) == 1:
            print (carts[0].x, carts[0].y)
            return

        # show(grid)
        ticks += 1


def main():

    input_data = read_input()
    carts = get_carts(input_data)
    grid = [list(l) for l in input_data]

    # show(grid)

    for cart in carts:
        grid[cart.y][cart.x] = reset_char(grid, cart.x, cart.y)
        grid[cart.y][cart.x] += cart.char

    crash_site = simulate(grid, carts)


if __name__ == '__main__':
    main()
