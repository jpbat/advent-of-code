
def main():

    line = input()

    idx = 0
    while idx < len(line) - 1:
        if abs(ord(line[idx]) - ord(line[idx + 1])) == 32:
            line = line[:idx] + line[idx + 2:]
            idx = max (0, idx - 1)
            continue

        idx += 1
    print (len(line))


if __name__ == '__main__':
    main()
