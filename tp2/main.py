from graph import Graph, Node

graph = Graph(directional=True)

graph.add_node(Node("A", ["B", "E"]))
graph.add_node(Node("B", ["C", "D"]))
graph.add_node(Node("C"))
graph.add_node(Node("D"))
graph.add_node(Node("E", ["D", "G", "F"]))
graph.add_node(Node("F", ["G"]))
graph.add_node(Node("G", ["C"]))

print(" ".join([x for x in graph.depth_first()]))