from UniformCostSearch import  uniform_cost_search
from Node import Node

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

def print_board(matrix):
    print('  | a b c d e f |')
    print('-----------------')
    for i in range(6):
        print(i, '| ', end='')
        for j in range(6):
            print(matrix[i][j] + ' ', end='')
        if (i != 2):
            print('|')
        else:
            print()
    print('-----------------')


if __name__ == '__main__':
    matrices = parse_file('sample_input_1.txt')
    print_board(matrices[0])

    root_node = Node(matrices[0], None, 0, {})
    print(root_node.cars)