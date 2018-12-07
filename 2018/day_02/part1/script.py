
def read_input():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def main():

    lines = read_input()

    rep_2_global = 0
    rep_3_global = 0

    for line in lines:

        rep_2 = 0
        rep_3 = 0
        repetitions = {}

        for letter in line:

            if letter in repetitions:
                continue

            repetitions[letter] = line.count(letter)

        for letter, n_repetitions in repetitions.items():

            if n_repetitions == 2:
                rep_2 = 1
            if n_repetitions == 3:
                rep_3 = 1

        rep_2_global += rep_2
        rep_3_global += rep_3

    print (rep_2_global * rep_3_global)


if __name__ == '__main__':
    main()
