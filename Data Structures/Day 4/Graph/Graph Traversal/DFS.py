#import deque from collections
from collections import deque

time = 0  # Global time for discovery/finish

#declaring color
WHITE = "WHITE"     #unvisted node
GRAY = "GRAY"       #visited, but it's all children[neighbours] are not visited
BLACK = "BLACK"     #visited and all of it's neighbours are visited

#defining a class for Vertex with attributes key, color, d and p
class Vertex(object):
    #constructor
    def __init__(self, key):
        self.key = key          #identifier
        self.color = WHITE      #to keep track of nodes
        self.d = 0              #discovery time
        self.f = 0              #finish time
        self.p = None           #predecessor of current node

    #return object in print
    def __str__(self):
        if self.p:
            pred = self.p.key
        else:
            pred = None
        return f"{self.key}: color={self.color}, d={self.d}, f={self.f} p={pred}"

#defining Graph class
class Graph(object):
    #constructor
    def __init__(self):
        self.adjList = {}           #adjacency list = {vertex : [neighbours]}

    #adding Vertex
    def addVertex(self, key):
        v = Vertex(key)             #creating a object from Vertex class
        self.adjList[v] = []
        return v

    #adding Edge
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)   #assuming graph is undirected

#Depth-First-Search
def dfs(G):
    global time
    time = 0

    #initialising all vertices at begining
    for u in G.adjList:
        u.color = WHITE
        u.p = None
    
    #for unvisted vertices calling dfs_visit
    #when there are more than 1 connected components exist in graph
    for u in G.adjList:
        if u.color == WHITE:    #unvisted
            dfsVisit(G, u)

def dfsVisit(G, u):
    global time
    time += 1
    u.d = time                  #set discovery time
    u.color = GRAY              #make it as visted, but neighbours are not visited
    print(u.key, end=' ')            #Output

    #visiting neighbours
    for v in G.adjList[u]:
        if v.color == WHITE:    #unvisted
            v.p = u
            dfsVisit(G, v)      #recursively calliing neighbours
    
    #after visiting all neighbours
    u.color = BLACK
    time += 1
    u.f = time                  #setting finish time

g = Graph()
A = g.addVertex('A')
S = g.addVertex('S')
B = g.addVertex('B')
C = g.addVertex('C')
D = g.addVertex('D')
E = g.addVertex('E')
F = g.addVertex('F')
G = g.addVertex('G')
H = g.addVertex('H')

g.addEdge(A, B)
g.addEdge(A, S)
g.addEdge(S, C)
g.addEdge(S, G)
g.addEdge(C, D)
g.addEdge(C, E)
g.addEdge(E, H)
g.addEdge(C, F)
g.addEdge(G, F)
g.addEdge(G, H)

print("DFS: ", end='')
dfs(g)