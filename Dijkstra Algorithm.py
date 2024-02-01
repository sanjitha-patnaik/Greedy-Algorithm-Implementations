# Dijkstra Algorithm

import heapq
def dijkstra(graph, start):
    # Initialize distances and visited set
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the minimum distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the node is already visited
        if current_node in visited:
            continue

        # Mark the node as visited
        visited.add(current_node)

        # Update distances to neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example Usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}: {result}")

