import math


def fuelRequired(vol):
    return math.floor(vol/3) - 2


def main():

    fullsum = 0

    while True:
        try:
            value = input()
            while True:
                requirement = fuelRequired(value)
                if requirement <= 0:
                    break
                value = requirement
                fullsum += requirement
        except EOFError:
            break

    print (fullsum)


if __name__ == '__main__':
    main()