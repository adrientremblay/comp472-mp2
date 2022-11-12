from copy import deepcopy
from filecmp import cmp

from car import Car

class Node:
    def __init__(self, board, parent, cost, fuel_levels):
        self.cars = {}
        self.board = board
        self.parent = parent
        self.cost = cost

        self.generate_cars(fuel_levels)

    def __eq__(self, other):
        self.cost == other.cost

    def __ne__(self, other):
        self.cost != other.cost

    def __lt__(self, other):
        self.cost < other.cost

    def __gt__(self, other):
        self.cost < other.cost

    def __le__(self, other):
        self.cost <= other.cost

    def __ge__(self, other):
        self.cost <= other.cost

    def generate_cars(self, fuel_levels):
        found_cars = []

        n = len(self.board) # should be 6
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == '.' or self.board[i][j] in found_cars:
                    continue

                fuel = fuel_levels[self.board[i][j]] if self.board[i][j] in fuel_levels else 100

                if j != n - 1 and self.board[i][j] == self.board[i][j+1]: # horizontal car
                    for k in range (j, n): # finding end of car
                        if k == n - 1 or self.board[i][k] != self.board[i][k+1]:
                            self.cars[self.board[i][j]] = Car(self.board[i][j], [i, j], [i, k], True, fuel)
                            break
                else: # must be a vertical car
                    for k in range (i, n): # finding end of car
                        if k == n - 1 or self.board[k][j] != self.board[k+1][j]:
                            self.cars[self.board[i][j]] = Car(self.board[i][j], [i, j], [k, j], False, fuel)
                            break

                found_cars.append(self.board[i][j])

    def is_goal_state(self):
        return self.board[2][5] == "A" and self.board[2][4] == "A"

    def generate_moves(self):
        moves = []

        for key in self.cars:
            car = self.cars[key]
            car_moves = self.generate_moves_for_car(car)
            moves += car_moves

        return moves

    def generate_moves_for_car(self, car):
        moves = []

        n = len(self.board) # should be 6
        if car.horizontal: # finding horizontal moves
            i = car.coord1[0]
            left = min(car.coord1[1], car.coord2[1])
            right = max(car.coord1[1], car.coord2[1])

            for j in range (left - 1, -1, -1): # finding moves to the left
                if self.board[i][j] != '.':
                    break
                new_node = deepcopy(self)
                to_put = right - left + 1
                for target in range(j, right+1):
                    if to_put > 0:
                        new_node.board[i][target] = car.name
                        to_put-=1
                    else:
                        new_node.board[i][target] = '.'
                new_node.cars[car.name].coord1[1] -= left - j
                new_node.cars[car.name].coord2[1] -= left - j
                new_node.cost += left - j
                new_node.parent = self
                moves.append(new_node)
            for j in range (right + 1, n): # finding moves to the right
                if self.board[i][j] != '.':
                    break
                new_node = deepcopy(self)
                to_put = right - left + 1
                for target in range(j, left-1, -1):
                    if to_put > 0:
                        new_node.board[i][target] = car.name
                        to_put-=1
                    else:
                        new_node.board[i][target] = '.'
                new_node.cars[car.name].coord1[1] += j - right
                new_node.cars[car.name].coord2[1] += j - right
                new_node.cost += j-right
                new_node.parent = self
                moves.append(new_node)
        else: # finding vertical moves
            j = car.coord1[1]
            top = min(car.coord1[0], car.coord2[0])
            bottom = max(car.coord1[0], car.coord2[0])

            for i in range (top - 1, -1, -1): # finding moves upwards
                if self.board[i][j] != '.':
                    break
                new_node = deepcopy(self)
                to_put = bottom - top + 1
                for target in range(i, bottom+1):
                    if to_put > 0:
                        new_node.board[target][j] = car.name
                        to_put-=1
                    else:
                        new_node.board[target][j] = '.'
                new_node.cars[car.name].coord1[0] -= top - i
                new_node.cars[car.name].coord2[0] -= top - i
                new_node.cost += top - i
                new_node.parent = self
                moves.append(new_node)
            for i in range (bottom + 1, n): # finding moves downwards
                if self.board[i][j] != '.':
                    break
                new_node = deepcopy(self)
                to_put = bottom - top + 1
                for target in range(i, top-1, -1):
                    if to_put > 0:
                        new_node.board[target][j] = car.name
                        to_put-=1
                    else:
                        new_node.board[target][j] = '.'
                new_node.cars[car.name].coord1[0] += i - bottom
                new_node.cars[car.name].coord2[0] += i - bottom
                new_node.cost += i - bottom
                new_node.parent = self
                moves.append(new_node)

        return moves

    def board_to_string(self):
        ret = '  | a b c d e f |\n'
        ret += '-----------------\n'
        for i in range(6):
            ret += str(i) + '| '
            for j in range(6):
                ret += self.board[i][j] + ' '
            if (i != 2):
                ret += '|\n'
            else:
                ret += '\n'
        ret += '-----------------\n'
        return ret

    def __repr__(self):
        ret = '    NODE...\n'
        ret += 'board:\n'
        ret += self.board_to_string()
        ret += 'cars:\n'
        ret += self.cars.__repr__() + '\n'
        return ret
