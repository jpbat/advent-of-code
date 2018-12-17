
class Node(object):

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def insert(base_node, value):

    new_node = Node(value)

    # skipping 1
    base_node = base_node.next

    new_node.next = base_node.next
    new_node.prev = base_node
    base_node.next.prev = new_node
    base_node.next = new_node

    return new_node


def retrieve(node, offset):

    for i in range(offset):
        node = node.prev

    previous_node = node.prev
    next_node = node.next

    previous_node.next = next_node
    next_node.prev = previous_node

    return next_node, node.value


def show(elf_playing, node, current_marble):

    print ('[{}] '.format(elf_playing), end='')

    while True:
        if current_marble == node:
            print ('({})'.format(node.value), end='')
        else:
            print (' {} '.format(node.value), end='')

        node = node.next

        if node.value == 0:
            break

    print()


def simulate(number_of_players, number_of_marbles):

    turn = 0

    node = Node(0)
    node.next = node
    node.prev = node
    base = node

    current_marble = node

    #show(0, base, current_marble)

    points = [0 for i in range(number_of_players)]

    while turn < number_of_marbles:

        elf_playing = turn % number_of_players + 1

        if (turn + 1) % 23 == 0:

            current_marble, aux = retrieve(current_marble, 7)
            points[elf_playing - 1] += turn + 1 + aux
            #show(elf_playing, base, current_marble)
            turn += 1
            continue

        current_marble = insert(current_marble, turn + 1)
        #show(elf_playing, base, current_marble)
        turn += 1

    print (max(points))


def main():

    input_data = input()

    number_of_players = int(input_data.split()[0])
    number_of_marbles = int(input_data.split()[-2])

    simulate(number_of_players, number_of_marbles)


if __name__ == '__main__':
    main()
