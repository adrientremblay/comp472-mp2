from uniform_cost_search import uniform_cost_search
from algo_a_astar import algo_a_astar
from node import Node

DEBUG = False
TEST_UCS = False
TEST_ALGO_ASTAR = True

import heuristics
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
#
def create_search_file(search_list, search_algo_name, test_number, heuristic_name="h1"):
    file_name = "output/" + search_algo_name
    if search_algo_name != "ucs":
        file_name += "-" + heuristic_name
    file_name += "-search-" + str(test_number) + ".txt"
    search_file = open(file_name, "w")
    for entry in search_list:
        message = "" + str(entry[0]) + " " + str(entry[1]) + " " + str(entry[2]) + " "
        if DEBUG:
            message+="\n"
        board = entry[3].board
        for i in range(0,6):
            for j in range(0, 6):
                message += board[i][j]
            if DEBUG:
                message+="\n"

        for key in entry[3].cars:
            car = entry[3].cars[key]
            if car.fuel == 100:
                continue
            message += " " + car.name + str(car.fuel)

        if DEBUG:
            message+="\n"

        search_file.write(message + "\n")
    search_file.close()


if __name__ == '__main__':
    test_root_nodes = parse_file('input.txt')

    tests_to_run = [2,3,4,5] # if empty then all root_nodes will be tested

    for i in range(len(test_root_nodes)):
        if len(tests_to_run) != 0 and not i in tests_to_run:
            continue

        print("Node To Test:")
        print()
        node_to_test = test_root_nodes[i]
        print(node_to_test)

        if TEST_UCS:
            print("Running Uniform Cost Search")
            solution, search_list = uniform_cost_search(node_to_test)
            create_search_file(search_list=search_list, search_algo_name="ucs", test_number=i+1)
            print("Final (Solved) Node:")
            print()
            print(solution)

        if TEST_ALGO_ASTAR:
            print("Running A Star Search")
            solution, search_list = algo_a_astar(node_to_test)
            create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1)
            print("Final (Solved) Node:")
            print()
            print(solution)