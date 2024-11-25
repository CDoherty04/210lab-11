"""
Name: Charlie Doherty
KUID: 3115329
EECS 210 Lab Session: Thursday 4-6
Lab: 11
Description: Program for implementing Dijkstra’s algorithm
Collaborators: None
"""


def dijkstra(graph, start, end):
    return graph, start, end


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

    print(dijkstra(graph1, "a", "b"))
    print(dijkstra(graph2, "a", "c"))
    print(dijkstra(graph3, "a", "e"))


main()
