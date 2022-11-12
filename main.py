from uniform_cost_search import  uniform_cost_search
from node import Node

def parse_line(line):
    board = [[0]*6 for i in range(6)] ;
    cur = 0;

    for i in range(6):
        for j in range(6):
            board[i][j] = line[cur];
            cur += 1

    fuel_levels = {}
    line_split = line.split(' ')
    for i in range(1, len(line_split)):
        string = line_split[i]
        fuel_levels[string[0]] = int(string[1])

    return Node(board, None, 0, fuel_levels)

def parse_file(file_name):
    nodes = [];

    file1 = open(file_name, 'r')
    lines = file1.readlines()

    for line in lines:
        if line == '\n' or line[0] == '#':
            continue

        nodes.append(parse_line(line))

    return nodes

if __name__ == '__main__':
    test_root_nodes = parse_file('input.txt')

    tests_to_run = [0] # if empty then all root_nodes will be tested

    for i in range(len(test_root_nodes)):
        if len(tests_to_run) != 0 and not i in tests_to_run:
            continue

        node_to_test = test_root_nodes[i]
        print(node_to_test)
        solution = uniform_cost_search(node_to_test)
        print(solution)