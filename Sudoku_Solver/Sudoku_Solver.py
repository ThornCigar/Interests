# This solver takes an 81 length string of 0-9 of sudoku puzzle, where 0 indicates an unfilled cell, and returns the
# solved board. Lots of improvements are yet to be made, e.g. checking for availability before each try. Recursion
# can also be employed but in this context it is a bit hard to conceptualise.


import re


f = open("Sudoku_problems.txt")  # Open txt file containing sudoku puzzles in the form of strings (0-9)
text = f.read()
raw = re.findall(r"(\d{9}.)", text, re.DOTALL)
for i in range(0, len(raw)):
    raw[i] = raw[i][0:9]
problems = []
counter = 0
temp = ""
for i in range(0, len(raw)):
    temp = temp + raw[i]
    if counter == 8:
        problems.append(temp)
        temp = ""
        counter = 0
    else:
        counter += 1
# The above part processes the text file to get the desired data structure, in this case list of strings


def convert(text_board):  # Convert string to list of integers
    return [int(i) for i in text_board]


def check(board):  # Check if a board is valid
    # Check rows
    for row in range(0, 9):  # Iterate over rows
        nums = set()  # Temporary storage for each iteration
        for i in range(row * 9, (row + 1) * 9):  # Iterate over cells in row
            if board[i] != 0:
                if board[i] not in nums:  # Add to nums if not in
                    nums.add(board[i])
                else:
                    return False  # Else row check failed

    # Check columns
    for col in range(0, 9):  # Iterate over columns
        nums = set()  # Temporary storage for each iteration
        for i in range(col, col + 73, 9):  # Iterate over cells in column
            if board[i] != 0:
                if board[i] not in nums:  # Add to nums if not in
                    nums.add(board[i])
                else:
                    return False  # Else column check failed

    # Check blocks
    for tl in [0, 3, 6, 27, 30, 33, 54, 57, 60]:  # # Iterate over top-left cells of blocks
        nums = set()  # # Temporary storage for each iteration
        block = list(range(tl, tl + 3)) + list(range(tl + 9, tl + 12)) + list(range(tl + 18, tl + 21))  # Make block
        for i in block:  # Iterate over cells in block
            if board[i] != 0:
                if board[i] not in nums:  # Add to nums if not in
                    nums.add(board[i])
                else:
                    return False  # Else column check failed

    return True  # Return True if all checks passed


def solve(text_board):
    board = convert(text_board)
    if len(board) != 81:  # Check board length
        print("Incorrect length.")
        return
    path = [0]  # Start from position 0
    while True:
        if not check(board):  # Check board first at beginning of while loop
            if board[path[-1]] == 9:  # If current cell is 9
                for i in range(len(path) - 1, -1, -1):  # Loop backward through cells visited
                    if board[path[i]] == 9:  # If cell is 9
                        board[path[i]] = 0  # Reset cell to 0
                        path.pop()  # Pop last visit history in path
                    else:  # First non-9 cell
                        board[path[i]] += 1  # Increment by 1
                        break  # Break after incrementing first non-9 cell
                continue  # Continue from beginning of while loop after reset/increment if board check failed
            else:
                board[path[-1]] += 1  # Else increment current cell by 1
                continue  # Continue from beginning of while loop after reset/increment if board check failed

        # Maybe do avail here?

        for i in range(path[-1], 81):
            if board[i] == 0:  # Find first 0 cell
                board[i] += 1  # Increment current cell by 1
                path.append(i)  # Append current position to path
                break  # Break, and proceed to beginning of while loop
            if i == 80:  # If no 0 found, board is solved, return board
                return board


def present(answer):
    for row in range(0, 9):
        for i in range(row * 9, row * 9 + 9):
            print(answer[i], end="  ")
        print("")


for i in range(0, len(problems)):
    board = problems[i]
    print("Board %s" % (str(i)))
    answer = solve(board)
    present(answer)
    print("")
