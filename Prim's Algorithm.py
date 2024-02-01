# Prim's Algorithm

import heapq
def prim(graph):
    start_vertex = list(graph.keys())[0]

    visited = set()
    min_spanning_tree = []
    priority_queue = [(0, None, start_vertex)]  # (weight, parent_vertex, current_vertex)

    while priority_queue:
        weight, parent_vertex, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        if parent_vertex is not None:
            min_spanning_tree.append((parent_vertex, current_vertex, weight))

        for neighbor, edge_weight in graph[current_vertex].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, current_vertex, neighbor))

    return min_spanning_tree

# Example Usage:
example_graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'D': 4, 'E': 3},
    'D': {'A': 3, 'B': 4, 'E': 1},
    'E': {'B': 3, 'D': 1}
}

result = prim(example_graph)

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in result:
    parent, child, weight = edge
    print(f"Edge: {parent} - {child}, Weight: {weight}")

