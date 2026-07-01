# Graph-Based Escape Route Optimizer

A Python implementation of a graph-based shortest path optimisation engine that computes the optimal escape route using Dijkstra's shortest path algorithm. The project features custom graph data structures, a binary min-heap priority queue, and efficient path reconstruction.

---

## Overview

This project models a weighted directed graph representing a forest escape scenario. Given a starting location, multiple possible exits, and special intermediate nodes (teleportation nodes) with unique traversal behaviour, the algorithm determines the minimum-cost escape path while satisfying all problem constraints.

Unlike a traditional shortest-path problem, a valid escape requires activating exactly one teleportation node before reaching an exit. This additional constraint transforms the problem into a more interesting pathfinding challenge, requiring the algorithm to optimise both travel cost and teleportation decisions.

---

## Example Graph

![Example Graph](images/dijkstra_example.svg)

**Figure 1.** Example directed weighted graph illustrating how the algorithm computes the shortest valid escape route by activating one teleportation node before reaching the exit.

---

## Features

- Weighted directed graph implemented using adjacency lists
- Custom `Graph`, `Vertex`, `Edge`, and `MinHeap` data structures
- Dijkstra's shortest path algorithm
- Efficient shortest-path reconstruction
- Support for teleportation nodes with additional traversal constraints
- Modular object-oriented architecture

---

## Technologies

- Python
- Graph Algorithms
- Dijkstra's Algorithm
- Binary Min Heap
- Object-Oriented Programming (OOP)

---

## Time Complexity

Let **V** denote the number of vertices and **E** denote the number of edges.

| Operation | Complexity |
| :--- | :---: |
| Graph Construction | **O(V + E)** |
| Dijkstra's Algorithm | **O(E log V)** |
| Space Complexity | **O(V + E)** |

---

## Project Structure

```text
graph-based-escape-route-optimizer/
│
├── examples/
│   ├── __init__.py
│   └── example_usage.py
│
├── images/
│   └── dijkstra_example.svg
│
├── src/
│   ├── __init__.py
│   ├── edge.py
│   ├── vertex.py
│   ├── heap.py
│   ├── graph.py
│   └── escape_route_optimizer.py
│
├── tests/
│   └── test_escape_route.py
│
├── LICENSE
├── README.md
└── .gitignore
```

---

## Example Usage

```python
from src import EscapeRouteOptimizer


roads = [
    (0, 1, 4),
    (0, 5, 12),
    (1, 2, 2),
    (2, 3, 2),
    (3, 4, 10),
    (3, 5, 2),
    (4, 5, 2),
]

teleportation_nodes = [
    (2, 2, 4),  # node, activation_cost, teleport_destination
]

optimizer = EscapeRouteOptimizer(roads, teleportation_nodes)

time_required, path = optimizer.escape(
    start=0,
    exits=[5],
)

print("Time required:", time_required)
print("Path:", path)
```

**Output**

```text
10
[0, 1, 2, 4, 5]
```

---

## Skills Demonstrated

- Graph modelling
- Shortest path optimisation
- Custom priority queue implementation
- Object-oriented software design
- Complexity analysis
- Algorithm implementation