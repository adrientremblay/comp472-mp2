from node import Node
from queue import PriorityQueue

def uniform_cost_search(start_node):
    open_list = PriorityQueue();
    open_list.put(start_node)
    closed_list = []

    while not open_list.empty():
        next_node = open_list.get()

        if next_node.is_goal_state():
            return next_node

        for child_node in next_node.generate_moves():
            # big assumption here that we consider a node to be visited if the board is the same
            # (the fuel levels may be different)
            if not child_node.board in closed_list:
                open_list.put(child_node)

        closed_list.append(child_node.board)

    return None
