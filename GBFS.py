from node import Node
from fifo_priority_queue import FifoPriorityQueue
import heuristics

def GBFS_algo(start_node, estimator=heuristics.check_heuristic1):
    open_list = FifoPriorityQueue()
    open_list.put(estimator(start_node.board), start_node)
    closed_list = []
    search_list = []

    while not open_list.is_empty():
        next_pair = open_list.get()

        if next_pair[1].is_goal_state():
            search_list.append((next_pair[0], next_pair[1].cost, estimator(next_pair[1].board), next_pair[1]))
            return next_pair, search_list

        for child_node in next_pair[1].generate_moves():
            if child_node.board in closed_list:
                continue

            open_list.put_with_replacement(estimator(child_node.board), child_node)

        closed_list.append(next_pair[1].board)
        search_list.append((next_pair[0], next_pair[1].cost, estimator(next_pair[1].board), next_pair[1]))

    return None, search_list
