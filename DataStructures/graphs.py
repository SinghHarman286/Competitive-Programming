'''Graph'''

class Graph:
    def __init__(self):
        self.graph = {}
    
    def addVertex(self, vertex):
        if not vertex in self.graph:
            self.graph[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if not vertex2 in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if not vertex1 in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
    
    def removeEdge(self, vertex1, vertex2):
        self.graph[vertex1] = list(filter(lambda vertex: vertex != vertex2, self.graph[vertex1]))
        self.graph[vertex2] = list(filter(lambda vertex: vertex != vertex1, self.graph[vertex2]))
    
    def removeVertex(self, vertex):
        if not vertex in self.graph.keys():
            return
        adjacentVertex = None
        while len(self.graph[vertex]):
            adjacentVertex = self.graph[vertex].pop()
            self.removeEdge(vertex, adjacentVertex)
        del self.graph[vertex]
    
    def dfsR(self, start):
        result = []
        visited = {}

        def dfs(vertex):
            visited[vertex] = True
            result.append(vertex)

            for adjacentVertex in self.graph[vertex]:
                if not adjacentVertex in visited:
                    dfs(adjacentVertex)
        
        dfs(start)

        print(result)

    def dfsI(self, vertex):
        stack = [vertex]
        visited = {}
        result = []
        visited[vertex] = True

        while stack:
            currentVertex = stack.pop()
            result.append(currentVertex)

            for adjacentVertex in self.graph[currentVertex]:
                if not adjacentVertex in visited:
                    visited[adjacentVertex] = True
                    stack.append(adjacentVertex)
        
        print(result)
    
    def bfs(self, vertex):
        queue = []
        result = []
        visited = {}
        queue.append(vertex)

        visited[vertex] = True

        while queue:
            currentVertex = queue.pop(0)
            result.append(currentVertex)

            for adjacentVertex in self.graph[currentVertex]:
                if not adjacentVertex in visited:
                    visited[adjacentVertex]= True
                    queue.append(adjacentVertex)
        
        print(result)




g = Graph()

g.addVertex("A")
g.addVertex("C")
g.addVertex("B")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B","D")
g.addEdge("C","E")
g.addEdge("D","E")
g.addEdge("D","F")
g.addEdge("E","F")

#           A
#         /   \
#        B     C
#        |     |
#        D --- E
#         \   /
#           F

print(g.graph)
print("=====")
g.dfsR("A")
print("=====")
g.dfsI("A")
print("=====")
g.bfs("F")
