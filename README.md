# Graph-Based Escape Route Optimizer

A Python implementation of a graph-based pathfinding engine that computes the optimal escape route using Dijkstra's shortest path algorithm. The project features custom graph data structures, a binary min-heap priority queue, and efficient path reconstruction.

---

## Overview

This project models a weighted directed graph representing a forest escape scenario. Given a starting location, multiple possible exits, and special intermediate nodes (Solulus) with unique traversal behaviour, the algorithm determines the minimum-cost escape path while satisfying all problem constraints.

---

## Features

- Weighted directed graph implemented using adjacency lists
- Custom `Graph`, `Vertex`, `Edge`, and `MinHeap` data structures
- Dijkstra's shortest path algorithm
- Efficient shortest-path reconstruction
- Support for special intermediate nodes with additional traversal constraints
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
|----------|------------|
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
├── README.md
└── .gitignore
```

---

## Example Usage

```python
from src import EscapeRouteOptimizer

roads = [
    (0, 1, 4),
    (1, 2, 3),
    (2, 3, 5),
    (0, 3, 15),
]

solulus = [
    (1, 2, 2),
]

escape_route = EscapeRouteOptimizer(roads, solulus)

time_required, path = escape_route.escape(
    start=0,
    exits=[3]
)

print(time_required)
print(path)
```

**Output**

```text
11
[0, 1, 2, 3]
```

---

## Skills Demonstrated

- Graph modelling
- Shortest path optimisation
- Priority queue implementation
- Object-oriented software design
- Complexity analysis
- Algorithm implementation