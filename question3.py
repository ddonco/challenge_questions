##### Question 3 #####
"""
Given an undirected graph G, find the minimum spanning tree
within G. A minimum spanning tree connects all vertices
in a graph with the smallest possible total weight of edges.
Your function should take in and return an adjacency list
structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function
definition should be question3(G)
"""
"""
Forked Node, Edge, and Graph classes from code built in lesson:
Technical Interview -> Graphs -> Graph Traversal Practice
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self._node_map = {}

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """
        Return a list of triples with the form:
        (Edge Value, From Node, To Node)
        """
        return [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]

    def get_adjacency_dict(self):
        """
        Return an adjacency dictionary with the form
        Node From: (To Node, Edge Value)
        """
        adjacency_lst = {}
        for edge in self.edges:
            if edge.node_from.value not in adjacency_lst:
                adjacency_lst[edge.node_from.value] = [(edge.node_to.value, edge.value)]
            else:
                adjacency_lst[edge.node_from.value].append((edge.node_to.value, edge.value))
        return adjacency_lst

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)

    def mst(self):
        """
        Build a Minimum Spanning Tree from the nodes and edges
        in the graph. Return a graph of the MST.
        """
        sorted_edges = sorted(self.edges, key=lambda edge: edge.value)
        mst = Graph()
        n = 0
        e = 0

        while n < len(self.nodes) and e < len(sorted_edges):
            next_edge = sorted_edges[e]
            e += 1
            mst_nodes = [node.value for node in mst.nodes]

            if n == 0 or (next_edge.node_to.value not in mst_nodes and
                          next_edge.node_from.value in mst_nodes):
                mst.insert_edge(next_edge.value, next_edge.node_from.value, next_edge.node_to.value)
                del sorted_edges[e]
                n += 1
                e = 0

        return mst


def question3(G):
    """
    Build a graph according to the provided adjacency dictionary.
    Find the minimum spanning tree of the graph. Return an
    adjacency dictionary of the MST.
    """
    graph = Graph()

    for node_from, edge in G.items():
        for i in edge:
            node_to = i[0]
            weight = i[1]
            graph.insert_edge(weight, node_from, node_to)

    min_span_tree = graph.mst()
    return min_span_tree.get_adjacency_dict()


def main():
    graph1 = {0: [(1, 20)],
              1: [(0, 20), (2, 50)],
              2: [(1, 50)]}
    print("Question3: {0}".format(question3(graph1)))
    # Result: {0: [(1, 20)],
    #          1: [(2, 50)]})

    graph2 = {0: [(1, 51), (3, 9950), (5, 10372)],
              1: [(0, 51), (3, 9900), (4, 9130)],
              2: [(3, 9217), (4, 932), (5, 9471)],
              3: [(0, 9950), (1, 9900), (2, 9217)],
              4: [(1, 9130), (2, 932)],
              5: [(0, 10375), (2, 9471)]}
    print("Question3: {0}".format(question3(graph2)))
    # Result: {0: [(1, 51)],
    #          1: [(4, 9130)],
    #          2: [(3, 9217), (5, 9471)],
    #          4: [(2, 932)]})

    graph3 = {0: [(1, 400), (7, 800)],
              1: [(2, 800), (0, 400), (7, 1100)],
              2: [(1, 800), (3, 700), (5, 400), (8, 200)],
              3: [(2, 700), (5, 1400), (4, 900)],
              4: [(3, 900), (5, 1000)],
              5: [(4, 1000), (3, 1400), (2, 400), (6, 200)],
              6: [(8, 600), (5, 200), (7, 100)],
              7: [(6, 100), (8, 700), (1, 1100), (0, 800)],
              8: [(7, 700), (6, 600), (2, 200)]
              }
    print("Question3: {0}".format(question3(graph3)))
    # Result: {1: [(0, 400)],
    #          2: [(8, 200), (3, 700), (1, 800)],
    #          3: [(4, 900)],
    #          5: [(2, 400)],
    #          6: [(7, 100), (5, 200)]})



if __name__ == '__main__':
    main()
