This assignment contains the code for a graph optimisation program.

**Overview of Contents**
- Introduction and Structure
- Libraries/Dependencies
- Execution Guide
- Description of Relevant Parts
- Summary
---

## 1. Introduction
This assignment belongs to the course "Algorithms and Data Structures 2". It was assigned by our professor Dr. Lyndon Nixon. The assignment's main goal is to cement our knowledge of different data structures, most importantly graphs and how we handle them, but also algorithms on how we solve the problem.
The goal is to input any graph, and have the output the same, but optimised graph. By optimisation we mean have a directed graph in which all vertices...
- have no more than 2 incoming edges to other vertices
- have no more than 2 outgoing edges to other vertices
- no vertex is disconnected (no in- or outdegree edges)
- as far as possible every vertex should have only exactly one indegree edge
- as far as possible every vertex should have only exactly one outdegree edge

## 2. Libraries/Dependencies
There are no additional libraries to installed outside of the Python standard library.

## 3. Execution Guide
If we want to execute the program, just take a look at the executable file "optimization.py". We can simply run it with the provided graph and it will output the optimised one, but feel free to modify the input. We can even provide and empty graph as input and the program will design a graph for us.
The way the graph input works is that firstly, the graph is a dictionary, where the keys are the vertices and the values are the outgoing edges to other vertices. This is an adjacency list representation, I chose it because I found it simpler for my solution, but the adjacency matrix version could be simpler if we want to directly find edges. In adjacency list, it's difficult to count the incoming edges to a vertex. Meaning, that for example this `graph["A"] = ["B", "C", "D"]` means that vertex A in the graph has 3 outgoing edges, to vertices B, C and D. If we want to count the incoming edges to a vertex, we have to search for the given vertex in the other adjacency lists, the total number gives us all the incoming edges to a vertex.

## 4. Description of Relevant Parts
In the file "methods.py" we have the basic necessary methods for adding edges, removing edges and checking if the graph is unconnected. There are also helper functions, one which checks if a graph is valid and one which checks if a new edge is valid (connect from a vertex to another vertex, these to vertices exist or not).
In "optimization.py" we have 3 key functions.
1. limit_indegree - Makes sure that in our graph no vertex has more than two indegree edges to other vertices.
2. limit_outdegree - Makes sure that in our graph no vertex has more than two outdegree edges to other vertices.
3. no_disconnected - Makes sure that in our graph no vertex is disconnected (disconnected = 0 in- or outdegree edges)
This program also contains the initial graph input and the final output.

## 5.Summary and Main Takeaways
In summary, I enjoyed working with graphs. It was always interesting how choosing different data structures or different algorithms would influence the outcome. I feel like I could ground my practical understanding better by doing this project.

If there was more time available, I would uograde my code like this:
- rewrite functions so they are more efficient and execution takes less time
- I overoptimised my graph, when the solution could have been easier (e.g. the description didn't say that all vertices had to be connected to another vertex, and there couldn't be circles)
- find a solution for adjacency matrices