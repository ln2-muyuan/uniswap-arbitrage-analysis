from collections import defaultdict


# BFS algorithm to check out if two nodes are connected
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

    def print_edges(self, n):
        print(self.edges[n])

    def is_reachable(self, s, d):
        visited = {}
        for i in self.nodes:
            visited[i] = False
        queue = [s]
        visited[s] = True
        while queue:
            n = queue.pop(0)  # pop the first element
            if n == d:
                return True
            for i in self.edges[n]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return False


a = Graph()
a.add_node('A')
a.add_node('B')
a.add_node('C')
a.add_node('D')
a.add_node('E')
a.add_node('F')
a.add_edge('A', 'B', 7)
a.add_edge('A', 'C', 9)
a.add_edge('A', 'F', 14)
a.add_edge('B', 'C', 10)
a.add_edge('B', 'D', 15)
a.add_edge('C', 'D', 11)
a.add_edge('C', 'F', 2)
a.add_edge('D', 'E', 6)
a.add_edge('E', 'F', 9)
# print(a.edges)
# print(a.distances)
# print(a.print_edges('A'))
print(a.is_reachable('A', 'E'))
print(a.is_reachable('A', 'G'))
