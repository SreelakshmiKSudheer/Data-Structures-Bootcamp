#import deque from collections
from collections import deque

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
        self.d = float('inf')   #distance from source [initialized with infinity]
        self.p = None           #predecessor of current node

    #return object in print
    def __str__(self):
        if self.p:
            pred = self.p.key
        else:
            pred = None
        return f"{self.key}: color={self.color}, d={self.d}, p={pred}"

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

#Breadth-First-Search
def bfs(G, s):
    #initialising all vertices at begining
    for u in G.adjList:
        u.color = WHITE
        u.d = float('inf')
        u.p = None

    #making start node just visited
    s.color = GRAY
    s.d = 0
    s.p = None

    #Creating an empty deque
    Q = deque()
    Q.append(s)

    while Q:                        #till deque is empty
        u = Q.popleft()             #u is the node whose neighbouring vertices are need to be found
        print(u.key, end = ' ')
        for v in G.adjList[u]:      #finding all neighbours v's of u from Adjacency List
            if v.color == WHITE:    #if v is unvisited
                v.color = GRAY      #making it as visited
                v.d = u.d + 1       #updating the distance from source
                v.p = u             #predecessor of v is u
                Q.append(v)
        u.color = BLACK             #all neighbours of u has been successfully visited


g = Graph()
A = g.addVertex('A')
B = g.addVertex('B')
C = g.addVertex('C')
D = g.addVertex('D')
E = g.addVertex('E')
F = g.addVertex('F')
G = g.addVertex('G')
g.addEdge(D, A)
g.addEdge(A, E)
g.addEdge(A, C)
g.addEdge(E, C)
g.addEdge(C, G)
g.addEdge(C, B)
g.addEdge(C, F)
g.addEdge(B, F)

print("BFS: ", end = ' ')
bfs(g, D)











        
