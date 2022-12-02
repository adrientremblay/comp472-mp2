from random import randint

if __name__ == '__main__':
    car_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    possible_orientations = ['h', 'v']
    random_puzzle_file_name = "Puzzles.txt"

    matrix = [['.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', 'X'],
              ['.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.']
              ]
    count_car_length_3 = 0
    for letter in car_letters:
        #Place the ambulance on the 3rd row first
        if letter == 'A':
            first_position = randint(0, 2)
            matrix[2][first_position] = 'A'
            matrix[2][first_position+1] = 'A'
        #For other cars
        else:
            #Choose randomly the length of the car and its orientation
            car_length = 2
            if count_car_length_3 < 3:
                car_length = randint(2, 3)

            car_orientation = possible_orientations[randint(0, 1)]

            #Set the maximum limit of position of X and Y for
            max_limit_x = 4
            max_limit_y = 4

            valid_position_found = False

            #Until it finds a valid position for this car, choose a random starting position
            while not valid_position_found:
                if car_length == 2:
                    #Generate the starting position
                    first_positionX = randint(0, max_limit_x)
                    first_positionY = randint(0, max_limit_y)

                    #If the car is horizontal, check if 1 position to the right is available
                    if car_orientation == 'h':
                        if matrix[first_positionX][first_positionY] == '.' and matrix[first_positionX+1][first_positionY] == '.':
                            matrix[first_positionX][first_positionY] = letter
                            matrix[first_positionX+1][first_positionY] = letter
                            valid_position_found = True
                    #Otherwise, check if 1 position down is available
                    else:
                        if matrix[first_positionX][first_positionY] == '.' and matrix[first_positionX][first_positionY+1] == '.':
                            matrix[first_positionX][first_positionY] = letter
                            matrix[first_positionX][first_positionY+1] = letter
                            valid_position_found = True
                #If the car is of length 3, then the max limits need to be changed
                else:
                    count_car_length_3 +=1
                    if car_orientation == 'h':
                        max_limit_x = 3
                        first_positionX = randint(0, max_limit_x)
                        first_positionY = randint(0, max_limit_y)
                        if matrix[first_positionX][first_positionY] == '.' and matrix[first_positionX+1][first_positionY] == '.' and matrix[first_positionX+2][first_positionY] == '.':
                            matrix[first_positionX][first_positionY] = letter
                            matrix[first_positionX+1][first_positionY] = letter
                            matrix[first_positionX+2][first_positionY] = letter
                            valid_position_found = True
                    else:
                        max_limit_y = 3
                        first_positionX = randint(0, max_limit_x)
                        first_positionY = randint(0, max_limit_y)
                        if matrix[first_positionX][first_positionY] == '.' and matrix[first_positionX][first_positionY+1] == '.' and matrix[first_positionX][first_positionY+2] == '.':
                            matrix[first_positionX][first_positionY] = letter
                            matrix[first_positionX][first_positionY+1] = letter
                            matrix[first_positionX][first_positionY+2] = letter
                            valid_position_found = True


    matrix[2][5] = '.'
    ret = '  | a b c d e f |\n'
    ret += '-----------------\n'
    for i in range(6):
        ret += str(i) + '| '
        for j in range(6):
            ret += matrix[i][j] + ' '
        if (i != 2):
            ret += '|\n'
        else:
            ret += '\n'
    ret += '-----------------\n'
    print(ret)

    matrix_in_string = ""
    for i in range(0,6):
        for j in range(0,6):
            matrix_in_string += matrix[i][j]
    print(matrix_in_string)

