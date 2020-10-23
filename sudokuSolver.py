import numpy as np

board = [[0, 7, 0, 8, 9, 0, 0, 0, 0],
         [0,5,0,0,0,0,3,0,4],
         [0,2,0,0,4,0,0,1,0],
         [5,6,8,9,0,0,4,7,2],
         [0,0,0,6,0,0,0,0,0],
         [1,0,7,0,5,0,6,3,8],
         [7,3,0,1,0,2,0,8,0],
         [6,0,0,4,7,0,1,0,0],
         [2,0,9,0,3,8,7,0,6]]


def print_board(board):
    for col_index in range (len(board)):
        if col_index != 0 and col_index % 3 == 0:
            print("---------------------------------")
        row = board[col_index]
        for row_index in range(len(row)) :
            if row_index != 0 and row_index % 3 == 0:
                print(" ", "|", end='')
            print(" ", row[row_index], end='')
        print("")


def possible(y, x, num):
    if num in board[y]:
        return False

    if num in np.array(board)[:, x]:
        return False

    row_start = (y // 3) * 3
    row_end = row_start + 3

    col_start = (x // 3) * 3
    col_end = col_start + 3

    # slice out 9 box array
    square_grid = np.array(board)[row_start:row_end, col_start:col_end]

    if num in square_grid.flatten():
        return False
    return True


def solve():
    for row_index in range(9):
        for col_index in range(9):
            if board[row_index][col_index] == 0:
                for num in range(1, 10):
                    if possible(row_index, col_index, num):
                        board[row_index][col_index] = num
                        solve()
                        # reset board
                        board[row_index][col_index] = 0
                return
    print_board(board)


if __name__ == '__main__':
    solve()



