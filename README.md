# AI Search Algorithms: Best-First Search and A* Search

This repository contains Python implementations of two popular AI search algorithms:
1. **Best-First Search**
2. **A* Search**

The algorithms are applied to a graph representing the map of Romania, with cities as nodes and distances between them as edges. The goal is to find the optimal path from a source city (e.g., `'Arad'`) to a destination city (e.g., `'Bucharest'`).

---

## Table of Contents
1. [Introduction](#introduction)
2. [Algorithms](#algorithms)
   - [Best-First Search](#best-first-search)
   - [A* Search](#a-search)
3. [Code Structure](#code-structure)
4. [How to Run](#how-to-run)


---

## Introduction
The project demonstrates how **Best-First Search** and **A* Search** can be used to solve pathfinding problems. The graph is represented as a dictionary, where each city maps to its neighbors and the distance to them. The algorithms use a **PriorityQueue** to prioritize nodes based on their heuristic value (Best-First Search) or total cost (A* Search).

---

## Algorithms

### Best-First Search
- **Heuristic**: Uses the straight-line distance to the goal (Bucharest) to guide the search.
- **Priority**: Nodes are prioritized based on their heuristic value.
- **Path Construction**: The path is built incrementally as the algorithm explores the graph.

### A* Search
- **Heuristic**: Uses the straight-line distance to the goal (Bucharest) as the heuristic.
- **Priority**: Nodes are prioritized based on the total cost \( f(n) = g(n) + h(n) \), where \( g(n) \) is the cost to reach the node and \( h(n) \) is the heuristic.
- **Path Construction**: The path is built incrementally as the algorithm explores the graph.

---

## Code Structure
The repository contains a single Python file:
- `bfs_and_a-star.py`: Implements both **Best-First Search** and **A* Search** algorithms.

### Key Components
1. **Heuristic Dictionary**: Stores the straight-line distance from each city to Bucharest.
2. **Graph Dictionary**: Represents the map of Romania with cities and distances.
3. **Best-First Search Function**: Implements the Best-First Search algorithm.
4. **A* Search Function**: Implements the A* Search algorithm.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Redoy0/AI-Search-Algorithms.git
   cd ai-search-algorithms
