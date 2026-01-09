class Graph:
    def __init__(self,numVertices):
        self.numVertices = numVertices
        self.adjMatrix = [[False for i in range(numVertices)] for j in range(numVertices)]

    def addEdge(self , i , j):
        self.adjMatrix[i][j]=True
        self.adjMatrix[j][i]=True   

    def printGraph(self):
       for i in range(self.numVertices):
        print(i, " : ", end="")
        for j in range(self.numVertices):
            print(1 if self.adjMatrix[i][j] else 0, end=" ")
        print()  # newline after finishing one row
   

g = Graph(4)   
g.addEdge(0,1)
g.addEdge(0,2) 
g.addEdge(1,2) 
g.addEdge(2,0) 
g.addEdge(2,3)  
g.printGraph()          

