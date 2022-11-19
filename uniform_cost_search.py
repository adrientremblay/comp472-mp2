from node import Node
from queue import PriorityQueue

def uniform_cost_search(start_node):
    open_list = PriorityQueue();
    open_list.put((start_node.cost, start_node))
    closed_list = []
    search_list = []

    while not open_list.empty():
        next_node = open_list.get()

        if next_node[1].is_goal_state():
            return next_node, search_list

        for child_node in next_node[1].generate_moves():
            # big assumption here that we consider a node to be visited if the board is the same
            # (the fuel levels for cars, cost of the node may be different)
            if child_node.board not in closed_list:
                open_list.put((child_node.cost, child_node))

        closed_list.append(next_node[1].board)
        # Todo: F(n) G(n) H(n)
        search_list.append((next_node[0], next_node[1].cost, next_node[1].board, next_node[1].board))

    return None, search_list
