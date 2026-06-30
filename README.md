# Graph-Based Escape Route Optimizer

A Python implementation of a weighted directed graph model using Dijkstra's algorithm to compute the fastest escape route under teleportation and destruction-time constraints.

## Algorithms and Data Structures

- Directed weighted graph using adjacency lists
- Dijkstra's shortest path algorithm
- Custom min-heap priority queue
- Path reconstruction using predecessor tracking

## Complexity

Let V be the number of trees and E be the number of roads.

- Graph construction: O(V + E)
- Shortest path computation: O(E log V)
- Space complexity: O(V + E)