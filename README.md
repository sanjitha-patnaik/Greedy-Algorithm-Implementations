# Greedy-Algorithm-Implementations

Fractional knapsack


Time Complexity

The time complexity of the greedy algorithm for the Fractional Knapsack Problem can be attributed to the following main steps:

Calculating value-to-weight ratios for each item: O(n), where n is the number of items.
Sorting the items based on the value-to-weight ratio: O(n log n) if a comparison-based sorting algorithm like QuickSort or MergeSort is used.
Iterating through the sorted items and adding items to the knapsack: O(n).
Therefore, the overall time complexity of the algorithm is dominated by the sorting step, making it O(n log n).



Space Complexity

The space complexity of the greedy algorithm is relatively low and primarily depends on the data structures used to represent the items and the knapsack.

O(n) space is required to store the list of items.

O(n) space is needed to store the value-to-weight ratios.

Hence, the space complexity of the algorithm is O(n).
