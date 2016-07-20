"""
Shortest path: Find the shortest path (of neighbors) from s to v for all v
"""
def shortest_path(s, v, memoize={}):
    """
    Brute force shortest path from v to s
    """
    if (s,v) in memoize:
        return memoize[(s,v)]
    shortest = None
    best_neighbor = None

    for neighbor in v.neighbors:
        possibly_shortest_path, next_neighbors = shortest_path(s, neighbor)
        possibly_shortest_path += v.dist(neighbor)
        if not shortest or possibly_shortest_path < shortest:
            path = next_neighbors + [neighbor]
            shortest = possibly_shortest_path

    if not shortest:
        return 0, [s]

    memoize[(s,v)] = (shortest, path)
    return shortest, path


def test_shortest_path():
    """
    Simple Graph to test
    S -> A -> B -> C -> V
      5    5    5     5

    Distance should be 20
    """
    s = SimpleDirectedNode({})
    a = SimpleDirectedNode({s:5})
    b = SimpleDirectedNode({a:5})
    c = SimpleDirectedNode({b:5})
    v = SimpleDirectedNode({c:5})

    calculated_shortest_distance = shortest_path(s, v)[0]
    assert(calculated_shortest_distance == 20)


class SimpleDirectedNode:
    def __init__(self, edges):
        self.neighbors = []
        self._weights = {}
        for node, weight in edges.items():
            self.neighbors.append(node)
            self._weights[node] = weight

    def dist(self, neighbor):
        return self._weights[neighbor]


if __name__ == "__main__":
    test_shortest_path()
