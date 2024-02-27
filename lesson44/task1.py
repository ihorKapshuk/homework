from module import Graph

# A---B
# |   |
# C---D---E

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("C", "D")
my_graph.add_edge("B", "D")
my_graph.add_edge("D", "E")

my_graph.show_graph()