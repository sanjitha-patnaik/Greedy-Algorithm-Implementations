# Policemen VS Thieves Problem

The goal is to catch thieves on a grid using a limited number of policemen. The policemen can catch thieves within a certain maximum distance 'k'. The code uses a brute-force approach to iterate through each cell with a policeman ('P') and check for thieves ('T') within the specified range.

# Time Complexity Analysis of the code :

The nested loops iterate through each cell in the grid, resulting in a time complexity of O(n^2), where 'n' is the size of the grid.
The inner loops iterate over a square region of side length '2k + 1' around each policeman. Therefore, the time complexity within each cell is O(k^2).
Overall, the time complexity of the catchThieves function is O(n^2 * k^2).


# Space Complexity Analysis of the code:

The space complexity is relatively low and constant, as the code only uses a 2D array of size 'n x n' to represent the grid. Thus, the space complexity is O(n^2).

# Performance Considerations:

The code uses a simple brute-force approach, which may not be efficient for large grids or values of 'k'.
It directly modifies the input grid ('C' for caught thieves), which may be undesirable in certain scenarios where the original grid needs to be preserved.
The algorithm stops iterating once all policemen run out ('policeCount == 0'), which can save some unnecessary iterations in specific cases.


# Potential Improvements:

We can optimize the algorithm to reduce the time complexity, especially for larger grids. This might involve a more advanced algorithmic approach.
The use of a data structure like priority queues or sorting the thieves based on their distance from policemen could potentially improve the efficiency of catching thieves.
For larger grids, parallelization or optimization techniques could be explored to enhance performance.
