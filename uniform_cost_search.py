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
            # big assumption here that we consider a node to be visited if the board is the same
            # (the fuel levels for cars, cost of the node may be different)
            if child_node.board not in closed_list:
                open_list.put(child_node.cost, child_node)

        closed_list.append(next_pair[1].board)
        # Todo: F(n) G(n) H(n)
        search_list.append((next_pair[0], next_pair[1].cost, 0, next_pair[1]))

    return None, search_list
