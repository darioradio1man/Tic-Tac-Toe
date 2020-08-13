the_list = list('         ')


def field(lst):
    print("---------", sep=" ")
    print(f"| {lst[0]} {lst[1]} {lst[2]} |", sep=" ")
    print(f"| {lst[3]} {lst[4]} {lst[5]} |", sep=" ")
    print(f"| {lst[6]} {lst[7]} {lst[8]} |", sep=" ")
    print("---------", sep=" ")


def coordinate_transform(coordinate):
    if coordinate == [1, 1]:
        return 6
    elif coordinate == [1, 2]:
        return 3
    elif coordinate == [1, 3]:
        return 0
    elif coordinate == [2, 1]:
        return 7
    elif coordinate == [2, 2]:
        return 4
    elif coordinate == [2, 3]:
        return 1
    elif coordinate == [3, 1]:
        return 8
    elif coordinate == [3, 2]:
        return 5
    elif coordinate == [3, 3]:
        return 2


def free_space_in_board(board, move):
    return board[move] == ' '


def is_full(board):
    for cell in range(0, 9):
        if free_space_in_board(board, cell):
            return False
    return True


def is_win(board, le):
    return (board[0] == le and board[1] == le and board[2] == le or
            board[3] == le and board[4] == le and board[5] == le or
            board[6] == le and board[7] == le and board[8] == le or
            board[0] == le and board[3] == le and board[6] == le or
            board[1] == le and board[4] == le and board[7] == le or
            board[2] == le and board[5] == le and board[8] == le or
            board[0] == le and board[4] == le and board[8] == le or
            board[2] == le and board[4] == le and board[6] == le
            )


def check_win(cells):
    x_num, o_num = 0, 0
    for i in range(0, 9):
        if cells[i] == "X":
            x_num += 1
        elif cells[i] == "O":
            o_num += 1
    if is_win(cells, "X") and is_win(cells, "O") or \
            not is_win(cells, "X") and not is_win(cells, "O") \
            and abs(x_num - o_num) >= 2:
        return "Impossible"
    elif is_win(cells, "X") and not is_win(cells, "O") and is_full(cells) or \
            is_win(cells, "X") and not is_win(cells, "O") and not is_full(cells):
        return "X wins"
    elif is_win(cells, "O") and not is_win(cells, "X") and is_full(cells) or \
            is_win(cells, "O") and not is_win(cells, "X") and not is_full(cells):
        return "O wins"
    elif not is_win(cells, "X") and not is_win(cells, "O") and is_full(cells) \
            and x_num + o_num == 9:
        return "Draw"
    elif not is_win(cells, "X") and not is_win(cells, "O") and not is_full(cells):
        return "Game not finished"


def check_input(cells):
    global step
    while check_win(cells) != "end":
        coord = input("Enter the coordinates: > ").split()
        try:
            coord = [int(i) for i in coord]
        except ValueError:
            print("You should enter numbers!")
            continue
        if len(coord) != 2:
            print("Please input two coordinates")
            continue
        elif coord[0] > 3 or coord[1] > 3 or coord[0] < 1 or coord[1] < 1:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            coordinates = coordinate_transform(coord)
            if cells[coordinates] == "X" or cells[coordinates] == "O":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                if step % 2 == 0:
                    cells[coordinates] = "O"
                    step += 1
                    break
                else:
                    cells[coordinates] = "X"
                    step += 1
                    break


step = 1
result = ""
field(the_list)
while check_win(the_list) == "Game not finished":
    check_input(the_list)
    field(the_list)
    result = check_win(the_list)
    if result != "Game not finished":
        print(result)



