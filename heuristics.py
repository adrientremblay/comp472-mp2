#Counts how many vehicles are in the way of the ambulance
def check_heuristic1(state, multiplier=1):
    list_vehicles = []
    i = 5
    while i >= 0:
        if state.board[2][i] == "A":
            break
        if state.board[2][i] != "." and state.board[2][i] not in list_vehicles:
            list_vehicles.append(state.board[2][i])
        i -= 1

    return len(list_vehicles)


#Counts how many positions are taken by cars other than ambulance
def check_heuristic2(state, multiplier=1):
    count = 0
    i = 5
    while i >= 0:
        if state.board[2][i] == "A":
            break
        if state.board[2][i] != ".":
            count += 1
        i -= 1
    return count


def check_heuristic3(state, multiplier=1):
    return check_heuristic1(state) * multiplier

#Temporary implementation of
"""
Proposed: Count all the cars in between the ambulance and the exit, and add 1 if the cars' orientation is not homogeneous.
"""
def check_heuristic4(state, multiplier=1):
    list_vehicles =[]
    i = 5
    while i >= 0:
        if state.board[2][i] == "A":
            break
        if state.board[2][i] != "." and state.board[2][i] not in list_vehicles:
            list_vehicles.append(state.board[2][i])
        i -= 1

    #Checks if the cars have different
    has_both_hor_vert=0
    if len(list_vehicles) > 0:
        is_horizontal = state.cars[list_vehicles[0]].horizontal
        for i in range(1,len(list_vehicles)):
            if state.cars[list_vehicles[i]].horizontal != is_horizontal:
                has_both_hor_vert = 1
                break
    return len(list_vehicles) + has_both_hor_vert

def heuristic_name_from_heuristic(heuristic):
    if heuristic == check_heuristic1:
        return "h1"
    elif heuristic == check_heuristic2:
        return "h2"
    elif heuristic == check_heuristic3:
        return "h3"
    elif heuristic == check_heuristic4:
        return "h4"
    return None

