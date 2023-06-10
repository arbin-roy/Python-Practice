class Graph:
    def __init__(self, gdict: dict = None):
        if gdict is None:
            self.gdict = {}
        else:
            self.gdict = gdict

    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False

    # def addEdge(self, vertex, edge):
    #     self.gdict[vertex].append(edge)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try:
                self.gdict[vertex1].remove(vertex2)
                self.gdict[vertex2].remove(vertex1)
                return True
            except ValueError:
                return False
        return False

    def remove_vertex(self, vertex):
        if vertex in self.gdict.keys():
            for i in self.gdict[vertex]:
                self.gdict[i].remove(vertex)
            del self.gdict[vertex]
            return True
        return False

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            dequeueVertex = queue.pop(0)
            print(dequeueVertex)
            for adjacentVertex in self.gdict[dequeueVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

    def printGraph(self):
        for vertex in self.gdict:
            print(vertex, ":", self.gdict[vertex])


cDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["c", "d", "f"],
    "f": ["d", "e"],
}
graph = Graph(cDict)

# graph = Graph()
# graph.addVertex("A")
# graph.addVertex("B")
# graph.addVertex("C")
# graph.addVertex("D")
# # graph.addEdge("e", "b")
# graph.add_edge("A", "B")
# graph.add_edge("B", "C")
# graph.add_edge("C", "A")
# graph.remove_edge("A", "D")
# graph.remove_vertex("D")
# graph.printGraph()
graph.dfs("a")
