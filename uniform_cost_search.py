from node import Node
from fifo_priority_queue import FifoPriorityQueue

def uniform_cost_search(start_node):
    open_list = FifoPriorityQueue();
    open_list.put(start_node.cost, start_node)
    closed_list = []
    search_list = []

    while not open_list.is_empty():
        next_pair = open_list.get()

        if next_pair[1].is_goal_state():
            search_list.append((next_pair[0], next_pair[1].cost, 0, next_pair[1]))
            return next_pair, search_list

        for child_node in next_pair[1].generate_moves():
            if child_node.board in closed_list:
                continue

            open_list.put_with_replacement(child_node.cost, child_node)

        closed_list.append(next_pair[1].board)
        search_list.append((next_pair[0], next_pair[0], 0, next_pair[1]))

    return None, search_list
