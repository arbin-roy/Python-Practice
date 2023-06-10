from collections import defaultdict


class Graph:
    def __init__(self, numOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        print(stack)


cGraph = Graph(8)
cGraph.addEdge("A", "C")
cGraph.addEdge("C", "E")
cGraph.addEdge("E", "H")
cGraph.addEdge("E", "F")
cGraph.addEdge("F", "G")
cGraph.addEdge("F", "G")
cGraph.addEdge("B", "D")
cGraph.addEdge("B", "C")
cGraph.addEdge("D", "F")

cGraph.topologicalSort()
