def read_input():

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def get_dependencies(lines):

    dependencies = {}
    for line in lines:
        before = line.split()[1]
        after = line.split()[7]

        if after not in dependencies:
            dependencies[after] = []

        if before not in dependencies:
            dependencies[before] = []

        dependencies[after].append(before)

    return dependencies


def main():

    dependencies = get_dependencies(read_input())

    solution = ""

    while len(dependencies.keys()) > 0:

        candidates = []

        for k, v in dependencies.items():

            if len(v) == 0:
                candidates.append(k)

        chosen = sorted(candidates)[0]

        for k, v in dependencies.items():
            if chosen in v:
                v.remove(chosen)

        solution += chosen
        del dependencies[chosen]

    print (solution)


if __name__ == '__main__':
    main()
