
def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def extract_patterns(data):

    positives = []
    negatives = []

    for d in data:
        pattern, result = d.replace('\n','').replace('\r','').split(' => ')
        if result == '#':
            positives.append(pattern)
        else:
            negatives.append(pattern)
    return negatives, positives


def simulate(initial_state, positive_patterns, negative_patterns):

    plants = initial_state
    offset = 0

    for generation in range(0, 20):
        offset = 6 * (generation + 1)

        new_plants = '....'
        plants = '....' + plants + '....'
        for i in range(2, len(plants) - 2):

            plant_pattern = plants[i-2:i+3]

            if plant_pattern in positive_patterns:
                new_plants += '#'
            else:
                new_plants += '.'
        new_plants += '....'
        plants = new_plants

    return plants, offset


def main():

    input_data = read_input()

    initial_state = input_data[0].replace('initial state: ','').replace('\r','')
    negative, positive = extract_patterns(input_data[2:])
    plants, offset = simulate(initial_state, positive, negative)

    idxs = []
    for i in range(len(plants)):
        if plants[i] == '#':
            idxs.append(i - offset)

    print (sum(idxs))


if __name__ == '__main__':
    main()
