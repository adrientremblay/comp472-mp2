from Car import Car

class Node:
    def __init__(self, board, parent, cost, fuel_levels):
        self.cars = {}
        self.board= board
        self.parent= parent
        self.cost = cost
        self.fuel_levels = fuel_levels

        self.generate_cars()

    def generate_cars(self):
        found_cars = []

        n = len(self.board) # should be 6
        for i in range(n):
            for j in range(n):
                if self.board[i][j] in found_cars:
                    continue

                if j != n - 1 and self.board[i][j] == self.board[i][j+1]: # horizontal car
                    for k in range (j, n): # finding end of car
                        if k == n - 1 or self.board[i][k] != self.board[i][k+1]:
                            self.cars[self.board[i][j]] = Car(self.board[i][j], [i, j], [i, k], True)
                            break
                else: # must be a vertical car
                    for k in range (i, n): # finding end of car
                        if k == n - 1 or self.board[k][j] != self.board[k+1][j]:
                            self.cars[self.board[i][j]] = Car(self.board[i][j], [i, j], [k, j], False)
                            break

                found_cars.append(self.board[i][j])

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
