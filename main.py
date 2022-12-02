from uniform_cost_search import uniform_cost_search
from algo_a_astar import algo_a_astar
from node import Node
from GBFS import GBFS_algo
from time import perf_counter
import csv

DEBUG = False
TEST_UCS = True
TEST_ALGO_ASTAR = False
TEST_GBFS = False

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
    input_lines = []

    file1 = open(file_name, 'r')
    lines = file1.readlines()

    for line in lines:
        if line == '\n' or line[0] == '#':
            continue

        input_lines.append(line)


        nodes.append(parse_line(line))

    return nodes,input_lines # added to capture line 
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



def create_solution_file(search_list, search_algo_name, test_number, node_to_test,lines,solution, eTime, heuristic_name="h1"):
    file_name = "output/" + search_algo_name
    if search_algo_name != "ucs":
        file_name += "-" + heuristic_name
    file_name += "-sol-" + str(test_number) + ".txt"
    soultion_file = open(file_name, "w")

    sol_txt = f"Initial Board Configuration: {lines} \n"
    sol_txt += f"{node_to_test.board_to_string()}\n" 
    sol_txt += f"Car fuel avalaible: {[(k,v.fuel) for (k,v) in sorted(node_to_test.cars.items())]} \n" # fuel
    sol_txt += f"Runtime: {round(eTime,1) } seconds \n" # uses time in the method
    sol_txt += f"Search path length: {len(search_list)} states\n" # search path
    sol_txt += f"Solution path length: moves \n" #missing
    sol_txt += f"Solution Path length: \n" #missing
    sol_txt += f"Solution Path: \n\n\n" #missing
    sol_txt += f"{solution.board_to_string()}\n" #solution board

    soultion_file.write(sol_txt)
    soultion_file.close()

if __name__ == '__main__':
    test_root_nodes, lines = parse_file('input.txt')

    tests_to_run = [0,1,2,3,4,5] # if empty then all root_nodes will be tested

    for i in range(len(test_root_nodes)):
        if len(tests_to_run) != 0 and not i in tests_to_run:
            continue
        print("Node To Test:")
        print()
        node_to_test = test_root_nodes[i]
       

        if TEST_UCS:
            print("Running Uniform Cost Search")

            start = perf_counter()
            solution, search_list = uniform_cost_search(node_to_test)
            end = perf_counter()
            create_search_file(search_list=search_list, search_algo_name="ucs", test_number=i+1)
            create_solution_file(search_list=search_list, search_algo_name="ucs", test_number=i+1,node_to_test = node_to_test,lines = lines[i],solution = solution[1],eTime= end-start)
            print("Final (Solved) Node:")
            print()
            print(solution)

        if TEST_ALGO_ASTAR:
            print("Running A Star Search")
            start = perf_counter()
            solution, search_list = algo_a_astar(node_to_test)
            end = perf_counter()
            create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1)
            create_solution_file(search_list=search_list, search_algo_name="ucs", test_number=i+1,node_to_test = node_to_test,lines = lines[i],solution = solution[1],eTime= end-start)
            print("Final (Solved) Node:")
            print()
            print(solution)
            #solution, search_list = algo_a_astar(node_to_test, estimator=heuristics.check_heuristic2)
            #create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1, heuristic_name="h2") 
            #solution, search_list = algo_a_astar(node_to_test, estimator=heuristics.check_heuristic3, mult = 5)
            #create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1, heuristic_name="h3") 
            #solution, search_list = algo_a_astar(node_to_test, estimator=heuristics.check_heuristic4)
            #create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1, heuristic_name="h4") 
     

        if TEST_GBFS:
            print("Running Greedy best first search")
            start = perf_counter()
            solution, search_list = GBFS_algo(node_to_test)
            end = perf_counter()
            create_search_file(search_list=search_list,search_algo_name="gbsf",test_number=i+1)
            create_solution_file(search_list=search_list, search_algo_name="ucs", test_number=i+1,node_to_test = node_to_test,lines = lines[i],solution = solution[1],eTime= end-start)
            print("Final (Solved) Node:")
            print()
            print(solution)
            #solution, search_list = GBFS_algo(node_to_test, estimator=heuristics.check_heuristic2)
            #create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1, heuristic_name="h2") 
            #solution, search_list = GBFS_algo(node_to_test, estimator=heuristics.check_heuristic3, mult = 5)
            #create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1, heuristic_name="h3") 
            #solution, search_list = GBFS_algo(node_to_test, estimator=heuristics.check_heuristic4)
            #create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1, heuristic_name="h4") 
        

