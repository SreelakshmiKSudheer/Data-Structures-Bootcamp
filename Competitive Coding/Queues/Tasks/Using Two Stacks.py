# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
queue = []
queries = []
for i in range(q):
    queries.append(list(map(int, input().rstrip().split())))
    
for query in queries:
    # print(query)
    if query[0] == 1:
        queue.append(query[1])
    elif query[0] == 2:
        queue.pop(0)
    elif query[0] == 3:
        print(queue[0])

'''
from collections import deque

q = int(input())
queue = deque()
for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        queue.append(query[1])
    elif query[0] == 2:
        queue.popleft()     
    elif query[0] == 3:
        print(queue[0]) 
'''