# Graph-Based Escape Route Optimizer

A Python implementation of a graph-based route optimizer using Dijkstra's shortest path algorithm, custom graph data structures, a custom min-heap, and path reconstruction.

## Overview

This project models a directed weighted forest map as a graph. Given a starting node, possible exit nodes, and special intermediate nodes that may change the route, the algorithm computes the fastest valid escape path.

## Features

- Directed weighted graph using adjacency lists
- Custom `Vertex`, `Edge`, `Graph`, and `MinHeap` classes
- Dijkstra's shortest path algorithm
- Path reconstruction using predecessor tracking
- Support for special intermediate nodes with additional traversal constraints

## Technologies

- Python
- Graph algorithms
- Dijkstra's algorithm
- Priority queues
- Object-oriented programming

## Complexity

Let `V` be the number of vertices and `E` be the number of edges.

- Graph construction: `O(V + E)`
- Dijkstra shortest path: `O(E log V)`
- Space complexity: `O(V + E)`

## Project Structure

```text
graph-based-escape-route-optimizer/
├── examples/
│   └── example_usage.py
├── src/
│   └── escape_route.py
├── tests/
│   └── test_escape_route.py
├── .gitignore
└── README.md