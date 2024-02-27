class Graph:

    def __init__(self) -> None:
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            print("Graph already contains this vertex")
            return False
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
        else:
            print("Graph is not containing one of this vertexes")
            return False
    
    def show_graph(self):
        for k, v in self.vertices.items():
            print(f"{k} -- {v}")