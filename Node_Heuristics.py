class Node:
    def __init__(self, board_state, parent_node):
        self.board_state = board_state
        self.parent_node = parent_node

    def __str__(self):
        return f"{self.board_state}"

    def is_goal_state(self):
        return self.board_state[2][5] == "A" and self.board_state[2][4] == "A"

#Counts how many vehicles are in the way of the ambulance
def check_heuristic1(state):
    list_vehicles = []
    i = 5
    while i >= 0:
        if state[2][i] == "A":
            break
        if state[2][i] != "." and state[2][i] not in list_vehicles:
            list_vehicles.append(state[2][i])
        i -= 1

    return len(list_vehicles)


#Counts how many positions are taken by cars other than ambulance
def check_heuristic2(state):
    count = 0
    i = 5
    while i >= 0:
        if state[2][i] == "A":
            break
        if state[2][i] != ".":
            count += 1
        i -= 1
    return count


def check_heuristic3(state, multipler = 1):
    return check_heuristic1(state) * multipler




#Temporary implementation of
def check_heuristic4(state):
    return 0
