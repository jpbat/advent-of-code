
def read_frequency_changes():
    frequencies = []
    while True:
        try:
            frequencies.append(int(input()))
        except EOFError:
            break
    return frequencies


def main():

    frequency = 0
    ocurrencies = {frequency: 1}
    frequency_changes = read_frequency_changes()

    idx = 0
    while True:

        frequency += frequency_changes[idx % len(frequency_changes)]

        if frequency in ocurrencies:
            print (frequency)
            break

        ocurrencies[frequency] = 1
        idx += 1


if __name__ == '__main__':
    main()