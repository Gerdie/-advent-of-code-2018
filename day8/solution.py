numbers = []
number_key = []

with open('input.txt') as input_file:
    current_number = None
    number_string = input_file.read()
    for char in number_string:
        if char in {' ', '\n', '\t'}:
            if current_number is not None:
                numbers.append(int(current_number))
            current_number = None
        else:
            if current_number is None:
                current_number = char
            else:
                current_number += char
    numbers.append(int(current_number))


class Node(object):
    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.children = []
        self.num_metadata = num_metadata
        self.metadata = []


nodes = []


def create_node(number_list):
    num_children = number_list[0]
    print('num children: {}'.format(num_children))
    num_metadata = number_list[1]
    print('num metadata: {}'.format(num_metadata))
    number_list.pop(0)
    number_list.pop(0)
    node = Node(num_children, num_metadata)
    for c in xrange(num_children):
        node.children.append(create_node(number_list))
    for m in xrange(num_metadata):
        print('metadata: {}'.format(number_list[0]))
        node.metadata.append(number_list[0])
        number_list.pop(0)

    return node


while numbers:
    nodes.append(create_node(numbers))

sum_metadata = 0
while nodes:
    node = nodes[-1]
    nodes.pop(-1)
    sum_metadata += sum(node.metadata)
    nodes.extend(node.children)


print('Part One: {}'.format(sum_metadata))
