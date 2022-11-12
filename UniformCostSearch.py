from Node import Node
from queue import PriorityQueue

def uniform_cost_search(start_node):
    open_list = PriorityQueue();
    open_list.put(start_node.cost, start_node)
    closed_list = []

    while not open_list.empty():
        next_node = open_list.get()

        if next_node.is_goal_state():
            return next_node

        for child_node in generateChildren(next_node):
            if not child_node.board_state in closed_list:
                open_list.put(child_node.cost, child_node)

        closed_list.append(next_node.board_state)

    return None

def generateChildren(node):
    board = node.board_state
    children = []



    return children
