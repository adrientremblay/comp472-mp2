from uniform_cost_search import  uniform_cost_search
from node import Node

def parse_matrix(matrix_line):
    ret = [[0]*6 for i in range(6)] ;
    cur = 0;

    for i in range(6):
        for j in range(6):
            ret[i][j] = matrix_line[cur];
            cur += 1

    return ret;

def parse_file(file_name):
    matrices = [];

    file1 = open(file_name, 'r')
    lines = file1.readlines()

    for line in lines:
        if line == '\n' or line[0] == '#':
            continue

        matrices.append(parse_matrix(line))

    return matrices


if __name__ == '__main__':
    test_boards = parse_file('sample_input_1.txt')

    root_node = Node(test_boards[0], None, 0, {})
    print (root_node)

    solution = uniform_cost_search(root_node)
    print(solution)