from uniform_cost_search import uniform_cost_search
from algo_a_astar import algo_a_astar
from node import Node
from GBFS import GBFS_algo
from time import perf_counter
import csv
import heuristics

DEBUG = False
TEST_UCS = True
TEST_ALGO_ASTAR = True
TEST_GBFS = True
GENERATE_SEARCH_FILE = False
GENERATE_SOLUTION_FILE = True
GENERATE_CSV = False

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
    
    no_solution = False
    try:
        solution = solution[1]
    except TypeError:
        solution = None
        no_solution = True

    solution_path = []
    cur = solution
    while cur is not None and cur.parent is not None:
        solution_path.insert(0 , cur)
        cur = cur.parent

    sol_txt = "--------------------------------------------------------------------------------\n\n"
    sol_txt += f"Initial Board Configuration: {lines} \n"
    sol_txt += f"{node_to_test.board_to_string()}\n" 
    sol_txt += f"Car fuel available: {[(k,v.fuel) for (k,v) in sorted(node_to_test.cars.items())]} \n" # fuel
    sol_txt += f"Runtime: {round(eTime,3) } seconds \n" # uses time in the method
    sol_txt += f"Search path length: {len(search_list)} states\n" # search path
    
    if no_solution:
        sol_txt += f"\n No solution found.\n"
    else:

        sol_txt += f"Solution path length: {len(solution_path)}\n" #missing
        sol_txt += f"Solution Path: " #missing
        for n in solution_path :
            sol_txt += n.move_name + "; " 
    
        sol_txt += f"\n\n"
    
        for n in solution_path :
            sol_txt += n.move_name + "\t" + str(n.move_fuel) + " "
            sol_txt += n.to_line() + " "
            sol_txt += n.list_cars_not_at_100()
            sol_txt += f"\n"   
        

        sol_txt += f"\n"
        sol_txt += f"{solution.board_to_string()}" #solution board
        sol_txt += str(solution.list_cars_not_at_100()) + "\n"
    sol_txt += "\n--------------------------------------------------------------------------------"

    soultion_file.write(sol_txt)
    soultion_file.close()


if __name__ == '__main__':
    test_root_nodes, lines = parse_file('input.txt')
    #test_root_nodes, lines = parse_file('random_puzzles.txt')

    tests_to_run = [] # if empty then all root_nodes will be tested
    heuristics_to_use = [heuristics.check_heuristic1, heuristics.check_heuristic2, heuristics.check_heuristic3, heuristics.check_heuristic4]

    csv_data = []

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

            if GENERATE_SEARCH_FILE:
                create_search_file(search_list=search_list, search_algo_name="ucs", test_number=i+1)
            if GENERATE_SOLUTION_FILE:
                create_solution_file(search_list=search_list, search_algo_name="ucs", test_number=i+1,node_to_test = node_to_test,lines = lines[i],solution = solution,eTime= end-start)
            if GENERATE_CSV:
                if solution is None:
                    csv_data.append([i+1, "UCS", "NA", "NA", "NA", node_to_test.to_line()])
                else:
                    cur = solution[1]
                    solution_length = 0;
                    while cur != None:
                       cur = cur.parent
                       solution_length += 1
                    csv_data.append([i+1, "UCS", "NA", solution_length, len(search_list), end - start, node_to_test.to_line()])

            print("Final (Solved) Node:")
            print()
            print(solution)


        if TEST_GBFS:
            for heuristic in heuristics_to_use:
                print("Running Greedy best first search")
                start = perf_counter()
                solution, search_list = GBFS_algo(node_to_test, estimator=heuristic)
                end = perf_counter()
                if GENERATE_SEARCH_FILE:
                    create_search_file(search_list=search_list,search_algo_name="gbfs",test_number=i+1, heuristic_name=heuristics.heuristic_name_from_heuristic(heuristic))
                if GENERATE_SOLUTION_FILE:
                    create_solution_file(search_list=search_list, search_algo_name="gbfs", test_number=i+1,node_to_test = node_to_test,lines = lines[i],solution = solution,eTime= end-start, heuristic_name=heuristics.heuristic_name_from_heuristic(heuristic))
                if GENERATE_CSV:
                    if solution is None:
                        csv_data.append([i+1, "UCS", "NA", "NA", "NA", node_to_test.to_line()])
                    else:
                        cur = solution[1]
                        solution_length = 0;
                        while cur != None:
                            cur = cur.parent
                            solution_length += 1
                        csv_data.append([i+1, "GBFS", heuristics.heuristic_name_from_heuristic(heuristic), solution_length, len(search_list), end - start, node_to_test.to_line()])
                print("Final (Solved) Node:")
                print()
                print(solution)
                
        if TEST_ALGO_ASTAR:
            for heuristic in heuristics_to_use:
                print("Running A Star Search")
                start = perf_counter()
                solution, search_list = algo_a_astar(node_to_test, heuristic)
                end = perf_counter()
                if GENERATE_SEARCH_FILE:
                    create_search_file(search_list=search_list,search_algo_name="a",test_number=i+1, heuristic_name=heuristics.heuristic_name_from_heuristic(heuristic))
                if GENERATE_SOLUTION_FILE:
                    create_solution_file(search_list=search_list, search_algo_name="a", test_number=i+1,node_to_test = node_to_test,lines = lines[i],solution = solution,eTime= end-start, heuristic_name=heuristics.heuristic_name_from_heuristic(heuristic))
                if GENERATE_CSV:
                    if solution is None:
                        csv_data.append([i+1, "UCS", "NA", "NA", "NA", node_to_test.to_line()])
                    else:
                        cur = solution[1]
                        solution_length = 0;
                        while cur != None:
                            cur = cur.parent
                            solution_length += 1
                        csv_data.append([i+1, "A/A*", heuristics.heuristic_name_from_heuristic(heuristic), solution_length, len(search_list), end - start, node_to_test.to_line()])
                print("Final (Solved) Node:")
                print()
                print(solution)

    if GENERATE_CSV:
        # stuff
        csv_header = ['Puzzle Number', 'Algorithm', 'Heuristic', 'Length of the Solution', 'Length of the Search Path', 'Execution Time (in seconds)', 'Board']
        with open('output/table.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(csv_header)

            # write multiple rows
            writer.writerows(csv_data)
