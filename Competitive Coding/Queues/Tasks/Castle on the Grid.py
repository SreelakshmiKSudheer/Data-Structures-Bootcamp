#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#
from collections import deque 

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    n = len(grid)
    queue = deque()
    queue.append((startX, startY, 0))
    visited = [[False] * n for _ in range(n)]
    visited[startX][startY] = True
    
    while queue:
        x, y, step = queue.popleft()
        if x == goalX and y == goalY:
            return step
        
        #  left
        for i in range(y-1, -1,-1):
            if grid[x][i] == 'X':
                break
            else:
                if not visited[x][i]:
                    visited[x][i] = True
                    queue.append((x,i,step + 1))
                
        #  right
        for i in range(y+1, n):
            if grid[x][i] == 'X':
                break
            else:
                if not visited[x][i]:
                    visited[x][i] = True
                    queue.append((x,i,step + 1))
                
        #  top
        for i in range(x-1, -1,-1):
            if grid[i][y] == 'X':
                break
            else:
                if not visited[i][y]:
                    visited[i][y] = True
                    queue.append((i,y,step + 1))
                
        #  bottom
        for i in range(x+1, n):
            if grid[i][y] == 'X':
                break
            else:
                if not visited[i][y]:
                    visited[i][y] = True
                    queue.append((i,y,step + 1))
                     
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
