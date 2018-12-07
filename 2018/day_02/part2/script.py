
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

    for i in range(len(lines)):
        for j in range(i, len(lines)):

            common = ''
            counter = 0

            for k in range(len(lines[i])):
                if lines[i][k] == lines[j][k]:
                    common += lines[i][k]
                else:
                    counter += 1

            if counter == 1:
                print (common)
                return


if __name__ == '__main__':
    main()
