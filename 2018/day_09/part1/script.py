
def show(elf_playing, board, current_marble_idx):

    print ('[{}] '.format(elf_playing), end='')


    for i in range(len(board)):
        if i == current_marble_idx:
            print ('({})'.format(board[i]), end='')
        else:
            print (' {} '.format(board[i]), end='')
    print()


def simulate(number_of_players, number_of_marbles):

    turn = 0
    board = [0]
    current_marble_idx = 0
    # show(0, board, current_marble_idx)
    points = [0 for i in range(number_of_players)]

    while turn < number_of_marbles:

        elf_playing = turn % number_of_players + 1

        if (turn + 1) % 23 == 0:
            points[elf_playing - 1] += turn + 1

            fetch_idx = current_marble_idx - 7
            points[elf_playing - 1] += board[fetch_idx]
            current_marble_idx = fetch_idx % len(board)
            del board[fetch_idx]
            #show(elf_playing, board, current_marble_idx)
            turn += 1
            continue

        insert_idx = (current_marble_idx + 2) % len(board)

        if insert_idx == 0:
            board.append(turn + 1)
            current_marble_idx = len(board) - 1
        else:
            board.insert(insert_idx, turn + 1)
            current_marble_idx = insert_idx

        #show(elf_playing, board, current_marble_idx)
        turn += 1

    print (max(points))



def main():

    input_data = input()

    number_of_players = int(input_data.split()[0])
    number_of_marbles = int(input_data.split()[-2])

    simulate(number_of_players, number_of_marbles)

if __name__ == '__main__':
    main()
