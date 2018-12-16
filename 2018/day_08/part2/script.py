
def read_node(id, data):

    number_of_childs = data.pop(0)
    number_of_metadata = data.pop(0)

    if number_of_childs == 0:
        node = {
            'id': id,
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
        'id': id,
        'childs': childs,
        'metadata': data[:number_of_metadata]
    }

    # print (node['id'], node['metadata'])
    return node, data[number_of_metadata:]


def get_node_value(tree_node):

    if len(tree_node['childs']) == 0:
        return sum(tree_node['metadata'])

    value_sources = []
    for meta_value in tree_node['metadata']:
        idx = meta_value - 1
        if idx < len(tree_node['childs']):
            value_sources.append(tree_node['childs'][idx])

    value = 0
    for child in value_sources:
        child_value = get_node_value(child)
        value += child_value
    return value


def main():

    data = [int(i) for i in input().split()]
    tree_root = read_node(ord('A'), data)[0]
    root_value = get_node_value (tree_root)
    print(root_value)


if __name__ == '__main__':
    main()
