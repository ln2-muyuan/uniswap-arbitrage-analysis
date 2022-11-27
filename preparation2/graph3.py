from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


a = Graph()
a.add_node('A')
a.add_node('B')
a.add_node('C')
a.add_node('D')
a.add_node('E')
a.add_node('F')
a.add_node('G')
a.add_node('H')
a.add_node('I')
a.add_edge('A', 'B', 7)
a.add_edge('A', 'C', 9)
a.add_edge('B', 'C', 10)
a.add_edge('B', 'D', 15)
a.add_edge('C', 'D', 11)
a.add_edge('C', 'F', 2)
a.add_edge('D', 'E', 6)
a.add_edge('E', 'F', 9)
a.add_edge('E', 'G', 9)
a.add_edge('G', 'H', 9)
a.add_edge('B', 'H', 9)


# length = nodes number in a path
def find_all_paths(graph, start, goal, length, current_path=[], all_paths=[]):
    current_path = current_path + [start]
    if start == goal:
        if len(current_path) <= length:
            all_paths.append(current_path)
    for node in graph.edges[start]:
        if node not in current_path:
            find_all_paths(graph, node, goal, length, current_path, all_paths)
    return all_paths


print(find_all_paths(a, 'A', 'H', 3))
