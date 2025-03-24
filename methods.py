###
# Methods here
###

# Checking if graph is a valid graph
def check_valid_graph(graph):
    # 1. Check if the graph is of dictionary type
    if not isinstance(graph, dict):
        raise ValueError(f"Invalid input: Not a graph! Expected a valid type of dictionary")
    # 2. Check if neighbors of a vertex is given as type list
    for vertex, neighbor in graph.items():
        if not isinstance(neighbor, list):
            raise ValueError(f"Not appropriate adjacency list for vertex {vertex}. "
                             f"Adjacency lists should be of type list.")
        # 2.1 Check if adjacency lists contain any vertex that is not represented in the graph
        for n in neighbor:
            if n not in graph:
                raise ValueError(f"Invalid Vertex Detected - Neighbor {n} is not a valid vertex in the graph")


# Check of valid vertex input
def edge_error_check(graph, vertex1, vertex2):
    # Check if edge 1 is missing/valid
    if vertex1 not in graph.keys():
        raise ValueError(f"{vertex1} is not represented in the graph! Enter a valid vertex!")
    # Check if edge2 is missing/valid
    elif vertex2 not in graph.keys():
        raise ValueError(f"{vertex2} not represented in the graph! Enter a valid vertex!")


# Function to add an edge to our graph
def ADD_EDGE(graph, start, to):
    # Check using methods the input (valid graph input + valid edges input)
    check_valid_graph(graph)
    edge_error_check(graph, start, to)

    # Adding the edge
    graph[start].append(to)
    # Give warning if we add a circle to our graph
    if start == to:
        print("WARNING! --- You just added a circle to your graph!")

    return graph


# Function to remove an edge from our graph
def REMOVE_EDGE(graph, start, to):
    # Check using methods the input (valid graph input + valid edges input)
    check_valid_graph(graph)
    edge_error_check(graph, start, to)

    # Remove an edge from a graph
    graph[start].remove(to)
    return graph


# Function to check unconnected edges and return a list
def CHECK_UNCONNECTED(graph):
    # Check valid graph input
    check_valid_graph(graph)

    # Creating a dictionary with the indegree edge count of all vertices
    indegree_count = {vertex: 0 for vertex in graph}
    for neighbors in graph.values():
        for n in neighbors:
            if n in indegree_count:
                indegree_count[n] += 1

    unconnected = []
    # Append vertex to list of unconnected vertices if both outdegree and indegree count is 0
    for vertex in graph:
        if len(graph[vertex]) == 0 and indegree_count[vertex] == 0:
            unconnected.append(vertex)

    return unconnected
