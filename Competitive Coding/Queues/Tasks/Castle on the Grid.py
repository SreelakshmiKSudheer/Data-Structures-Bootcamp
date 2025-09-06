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
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    q = deque()
    
    q.append((startX, startY, 0))
    visited[startX][startY] = True
    
    while q:
        x, y, steps = q.popleft()
        
        # Goal reached
        if x == goalX and y == goalY:
            return steps
        
        # Explore 4 directions like rook
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x, y
            # Move until obstacle/edge
            while 0 <= nx+dx < n and 0 <= ny+dy < n and grid[nx+dx][ny+dy] != 'X':
                nx += dx
                ny += dy
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, steps+1))                    
                
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
