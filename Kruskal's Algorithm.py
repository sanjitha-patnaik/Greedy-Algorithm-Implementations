# Kruskal's Algorithm

class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((weight, vertex, neighbor))

    edges.sort()  # Sort edges in ascending order by weight
    vertices = set(vertex for edge in edges for vertex in edge[1:3])
    minimum_spanning_tree = []
    union_find = UnionFind(vertices)

    for weight, vertex1, vertex2 in edges:
        if union_find.find(vertex1) != union_find.find(vertex2):
            union_find.union(vertex1, vertex2)
            minimum_spanning_tree.append((vertex1, vertex2, weight))

    return minimum_spanning_tree

# Example Usage:
example_graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'D': 4, 'E': 3},
    'D': {'A': 3, 'B': 4, 'E': 1},
    'E': {'B': 3, 'D': 1}
}

result = kruskal(example_graph)

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in result:
    vertex1, vertex2, weight = edge
    print(f"Edge: {vertex1} - {vertex2}, Weight: {weight}")

