import math

def main():

    fullsum = 0

    while True:
        try:
            fullsum += math.floor(input()/3) - 2
        except EOFError:
            break

    print (fullsum)


if __name__ == '__main__':
    main()