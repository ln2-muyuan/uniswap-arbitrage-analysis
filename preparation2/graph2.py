from collections import defaultdict


# DFS algorithm to check out if two nodes are connected
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

    def is_reachable(self, s, d):
        visited = {}
        for i in self.nodes:
            visited[i] = False
        stack = [s]
        visited[s] = True
        while stack:
            n = stack.pop()     # pop the last element
            if n == d:
                return True
            for i in self.edges[n]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
