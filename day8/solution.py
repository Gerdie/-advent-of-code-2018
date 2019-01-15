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
        self.value = 0

    def calculate_value(self):
        if not self.children:
            self.value = sum(self.metadata)
        else:
            for metadata in self.metadata:
                try:
                    self.value += self.children[metadata - 1].value
                except IndexError:
                    pass


nodes = []


def create_node(number_list):
    num_children = number_list[0]
    num_metadata = number_list[1]
    number_list.pop(0)
    number_list.pop(0)
    node = Node(num_children, num_metadata)
    for c in xrange(num_children):
        node.children.append(create_node(number_list))
    for m in xrange(num_metadata):
        node.metadata.append(number_list[0])
        number_list.pop(0)
    node.calculate_value()
    return node


while numbers:
    nodes.append(create_node(numbers))

root_value = None
sum_metadata = 0
while nodes:
    node = nodes[-1]
    nodes.pop(-1)
    sum_metadata += sum(node.metadata)
    nodes.extend(node.children)
    if root_value is None:
        root_value = node.value


print('Part One: {}'.format(sum_metadata))
print('Part Two: {}'.format(root_value))
