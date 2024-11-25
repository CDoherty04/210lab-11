"""
Name: Charlie Doherty
KUID: 3115329
EECS 210 Lab Session: Thursday 4-6
Lab: 11
Description: Program for implementing Dijkstra’s algorithm
Collaborators: None
"""


def dijkstra(graph, start, end):

    n = len(graph)
    # ord(char) returns the ASCII int value of a char
    start = ord(start)-97
    end = ord(end)-97
    L = [float('inf')] * n
    previous_nodes = [None] * n
    L[start] = 0
    S = list(range(n))  # List of unvisited nodes

    while S:
        # Find the node with the smallest distance
        current_node = min(S, key=lambda node: L[node])

        # Stop if the end node is reached or no reachable nodes remain
        if current_node == end or L[current_node] == float('inf'):
            break

        S.remove(current_node)

        # Update distances to neighbors
        for neighbor, weight in enumerate(graph[current_node]):
            if weight != -1 and neighbor in S:
                new_distance = L[current_node] + weight
                if new_distance < L[neighbor]:
                    L[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return L[end], path


def main():
    graph1 = [[-1, 6, 3, -1],
              [6, -1, 4, 1],
              [3, 4, -1, 1],
              [-1, 1, 1, -1]]

    graph2 = [[-1, 2, -1, 8, -1, -1],
              [2, -1, -1, 5, 6, -1],
              [-1, -1, -1, -1, 9, 3],
              [8, 5, -1, -1, 3, 2],
              [-1, 6, 9, 3, -1, 1],
              [-1, -1, 3, 2, 1, -1]]

    graph3 = [[-1, 3, 20, 12, -1, -1],
              [3, -1, -1, 5, -1, -1],
              [20, -1, -1, 9, 2, -1],
              [12, 5, 9, -1, -1, 7],
              [-1, -1, 2, -1, -1, 8],
              [-1, -1, -1, 7, 8, -1]]


    # MODIFY THIS LINE FOR DIFFERENT GRAPHS
    distance, path = dijkstra(graph1, 'a', 'b')


    # Map numeric nodes back to letters
    node_labels = ['a', 'b', 'c', 'd']
    path_labels = [node_labels[node] for node in path]

    print(f"Path is {distance} units long, and goes from {", ".join(path_labels)}")


main()
