import numpy as np
import random


board = np.zeros((9, 9), dtype=int)

for i in range(0, 9, 3):
    nums = list(range(1, 10))
    random.shuffle(nums)
    for r in range(3):
        for c in range(3):
            board[i+r][i+c] = nums.pop()


row, col = 0, 0
while row < 9:
    while col < 9:
        if board[row][col] == 0:  
            for num in range(1, 10):
                if (
                    num not in board[row] and  
                    num not in board[:, col] and  
                    num not in board[(row//3)*3:(row//3)*3+3, (col//3)*3:(col//3)*3+3]  # Check 3x3 box
                ):
                    board[row][col] = num
                    break
        col += 1
    row += 1


num_holes = random.randint(40, 50)
for _ in range(num_holes):
    row, col = random.randint(0, 8), random.randint(0, 8)
    board[row][col] = 0


for row in board:
    print(" ".join(str(num) if num != 0 else "." for num in row))
