

def main():

    frequency = 0

    while True:
        try:
            frequency += int(input())
        except EOFError:
            break

    print (frequency)


if __name__ == '__main__':
    main()