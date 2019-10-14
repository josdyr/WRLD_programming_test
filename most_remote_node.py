import math
import time


file0 = "problem_small.txt"
file1 = "problem_big.txt"

class Node:

    nearest_neighbour_length = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def get_length(current_node, node):
    delta_x = abs(node.x - current_node.x)
    delta_y = abs(node.y - current_node.y)
    return math.sqrt(delta_x**2 + delta_y**2)

def get_nearest_neighbour_length(current_node, all_nodes):
    # loop through all nodes again: n^2 (all neighbours of current node)
        # get nearest neighbour
        # get the length of that nearest neighbour
    length = math.inf
    for node in all_nodes:
        current_length = get_length(current_node, node)
        if current_length < length and current_length != 0:
            length = get_length(current_node, node)

    return length

def get_most_remote_node():

    all_nodes = []

    with open(file1) as f:
        for line in f: # loop through all lines/nodes
            x = int(line[:-1].split(sep=" ")[1])
            y = int(line[:-1].split(sep=" ")[2])
            all_nodes.append(Node(x, y))

    highest_nearest_neighbour_length = 0
    most_remote_node = None
    for node in all_nodes:

        start = time.time()

        node.nearest_neighbour_length = get_nearest_neighbour_length(node, all_nodes)
        if node.nearest_neighbour_length > highest_nearest_neighbour_length:
            highest_nearest_neighbour_length = node.nearest_neighbour_length
            most_remote_node = node

        end = time.time()
        print(end - start)

    # return the node that has the highest nearest_neighbour_length
    import ipdb; ipdb.set_trace()
    return most_remote_node

def main():
    # input data
        # read file: problem_small.txt
    # loop through all nodes
        # save distance to nearest neighbour
            # calculate the largest Euclidian distance
    # return node with highest value for nearest neighbour

     return get_most_remote_node()


if __name__ == '__main__':
    main()
