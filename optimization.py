from methods import ADD_EDGE, REMOVE_EDGE, CHECK_UNCONNECTED

graph = dict()
graph["A"] = ["B", "C", "D"]
graph["B"] = ["D", "G", "F"]
graph["C"] = ["E", "H", "G"]
graph["D"] = ["H", "M"]
graph["E"] = ["A", "I", "L"]
graph["F"] = ["J", "N"]
graph["G"] = ["J", "K"]
graph["H"] = ["O"]
graph["I"] = ["G", "H"]
graph["J"] = ["B", "K"]
graph["K"] = ["F", "L"]
graph["L"] = ["P"]
graph["M"] = ["L", "O"]
graph["N"] = ["P", "K"]
graph["O"] = ["N", "L"]
graph["P"] = ["M", "K", "I", "O"]
print(f"Input graph: \n{graph}")

# 1. No vertex has more than two indegree edges to other vertices
def limit_indegree(input_graph):
    # Creating an indegree count dictionary and calculating separately
    indegree_count = {vertex: 0 for vertex in input_graph}
    for neighbors in input_graph.values():
        for n in neighbors:
            if n in indegree_count:
                indegree_count[n] += 1
    # Checking the vertices that have +2 indegree edges, and we reduce them
    for vertex, count in indegree_count.items():
        if count > 1:
            extra = count-1
            for vertex_in, neighbors in input_graph.items():
                if vertex in neighbors:
                    REMOVE_EDGE(input_graph, vertex_in, vertex)
                    extra -= 1
                    if extra == 0:
                        break
    return input_graph


graph = limit_indegree(graph)

# 2. No vertex has more than two outdegree edges to other vertices
def limit_outdegree(input_graph):
    for vertex, neighbors in input_graph.items():
        # If outdegree count of a vertex is greater than 1, we loop through its outdegree edges and use some logic to
        # remove edges.
        while len(neighbors) > 1:
            # I'm sorting the adjacency list of the vertex, so that it results in descending order based on each
            # neighbor's appearance in other adjacency lists -> remove the last one in the row, because it has the
            # lowest number of occurrences (reverse=True ->  order descending ).
            # -> This way I am making more refined changes instead of randomly deleting an edge
            sorted_neighbors = sorted(
                neighbors,
                key=lambda neighbor: sum(neighbor in n for n in input_graph.values()),
                reverse=True)
            REMOVE_EDGE(input_graph, vertex, sorted_neighbors[-1])
    return input_graph


graph = limit_outdegree(graph)


def no_disconnected(input_graph):
    # Create indegree_count dictionary
    indegree_count = {vertex: 0 for vertex in input_graph}
    for neighbors in input_graph.values():
        for n in neighbors:
            if n in indegree_count:
                indegree_count[n] += 1

    # Create outdegree_count dictionary
    outdegree_count = {vertex: len(neighbors) for vertex, neighbors in input_graph.items()}
    # Create unconnected vertices list
    unconnected_list = CHECK_UNCONNECTED(input_graph)

    # While unconnected_list is not empty
    while unconnected_list:
        candidate = None

        # We assign a vertex as candidate if its outdegree and indegree count is less than 2
        # candidate will be used to connect "lonely edges"
        for v in indegree_count:
            if outdegree_count[v] < 2 and indegree_count[v] < 2:
                candidate = v
                break

        # Take an unconnected vertex from the list
        for vertex in unconnected_list:
            # We make sure that we don't create circles or connect edges that would create in- or outdegree counts >= 3
            if vertex != candidate and indegree_count[vertex] < 2 and indegree_count[candidate] < 2:
                ADD_EDGE(input_graph, vertex, candidate)
                # We increment the indegree count of the candidate and outdegree count of vertex by +1
                indegree_count[candidate] += 1
                outdegree_count[vertex] += 1
        # Refresh unconnected_list
        unconnected_list = CHECK_UNCONNECTED(input_graph)

    # We assign a target for adding an edge to those vertices that have 0 outdegree
    # (aim: keep every vertex intact => graph in one unit)
    for out in outdegree_count:
        if outdegree_count[out] == 0:
            target = None
            for v in indegree_count:
                # making sure that our target doesn't already have more than 1 indegree edge (Rule #1)
                if indegree_count[v] < 2 and v != out:
                    target = v
                    break
            # If target exists, we add an edge between a vertex with 0 outdegree to a vertex with less than 2 indegree
            if target:
                ADD_EDGE(input_graph, out, target)
                # Increment indegree count of target vertex by +1 and outdegree count of "out" vertex by +1
                indegree_count[target] += 1
                outdegree_count[out] += 1
    return input_graph


graph = no_disconnected(graph)
print(f"Final graph: \n{graph}")
