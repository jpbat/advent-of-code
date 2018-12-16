
def read_node(id, data):

    number_of_childs = data.pop(0)
    number_of_metadata = data.pop(0)

    if number_of_childs == 0:
        node = {
            'id': chr(id),
            'childs': [],
            'metadata': data[:number_of_metadata]
        }
        remaining_data = data[number_of_metadata:]
        return node, remaining_data

    childs = []
    for i in range(number_of_childs):
        child, data = read_node(id + i + 1, data)
        childs.append(child)

    node = {
        'id': chr(id),
        'childs': childs,
        'metadata': data[:number_of_metadata]
    }

    # print (node['id'], node['metadata'])
    return node, data[number_of_metadata:]


def get_metadata(tree_node, metadata_sum):

    metadata_sum += sum(tree_node['metadata'])
    for child in tree_node['childs']:
        metadata_sum = get_metadata(child, metadata_sum)
    return metadata_sum


def main():

    data = [int(i) for i in input().split()]
    tree_root = read_node(ord('A'), data)[0]
    metadata_sum = get_metadata (tree_root, 0)
    print(metadata_sum)


if __name__ == '__main__':
    main()
