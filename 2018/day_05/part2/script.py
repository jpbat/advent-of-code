
def react(polymer):

    idx = 0
    while idx < len(polymer) - 1:
        if abs(ord(polymer[idx]) - ord(polymer[idx + 1])) == 32:
            polymer = polymer[:idx] + polymer[idx + 2:]
            idx = max (0, idx - 1)
            continue

        idx += 1

    return polymer


def extract_units(polymer):

    units = []

    for unit in polymer:
        if ord(unit) < ord('Z') and unit not in units:
            units.append(unit)

    return units


def main():

    line = input()
    units = extract_units(line)

    min_length = len(line)
    for unit in units:
        length = len(react(line.replace(unit, '').replace(unit.lower(), '')))
        if length < min_length:
            min_length = length

    print (min_length)

if __name__ == '__main__':
    main()
