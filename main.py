def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def parse_matrix(matrix_line):
    ret = [[0]*6 for i in range(6)] ;
    cur = 0;

    for i in range(6):
        for j in range(6):
            ret[i][j] = matrix_line[cur];
            cur += 1

    return ret;

def parse_file(file_name):
    matrices = [];

    file1 = open(file_name, 'r')
    lines = file1.readlines()

    for line in lines:
        if line == '\n' or line[0] == '#':
            continue

        matrices.append(parse_matrix(line))

    return matrices

def print_board(matrix):
    print('  | a b c d e f |')
    print('-----------------')
    for i in range(6):
        print(i, '| ', end='')
        for j in range(6):
            print(matrix[i][j] + ' ', end='')
        print('|')
    print('-----------------')


if __name__ == '__main__':
    matrices = parse_file('sample_input_1.txt')
    print_board(matrices[0])