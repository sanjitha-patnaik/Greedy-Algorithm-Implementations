# Kruskal's Algorithm:
Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a connected, undirected graph with weighted edges. The minimum spanning tree is a subset of the edges that forms a tree including all the vertices of the graph while minimizing the total edge weight. Kruskal's algorithm builds the minimum spanning tree by iteratively adding the smallest edge that does not create a cycle in the growing forest of edges.


# Algorithm Steps:

## Initialization:
Start with all vertices as separate trees (disjoint sets).
Sort the edges in ascending order based on their weights.

## Growing the Tree:
Iterate through the sorted edges and add the smallest edge that does not form a cycle.
Use a disjoint-set data structure (e.g., Union-Find) to efficiently check for cycles.

## Termination:
Continue until all vertices are part of a single connected component, forming the minimum spanning tree.



# Time Complexity:
With the use of Union-Find data structure for cycle detection and a sorting step, Kruskal's algorithm has a time complexity of O(E log E), where E is the number of edges.
The dominant factor is often the sorting step.


# Space Complexity:
The space complexity is O(V + E), where V is the number of vertices and E is the number of edges.
This includes the space required for the disjoint-set data structure and the sorted edges.



# Applications:

## Network Design:
Used in designing communication networks, electrical grids, and transportation networks with minimum overall cost.

## Circuit Design:
Applied in designing electronic circuits to minimize the total wire length.

## Resource Management:
Used in resource allocation problems where connecting resources with minimum cost is crucial.

## Routing Protocols:
Applied in network routing protocols to find efficient paths with minimum latency.

## Wireless Sensor Networks:
Used in wireless sensor networks to optimize communication between sensor nodes.

## Urban Planning:
Applied in urban planning for designing efficient road networks.
