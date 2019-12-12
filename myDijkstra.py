#!usr/bin/env python3

import heapq
import sys

from utils import readAdjacencyMatrix, pathString


def main():
    adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_4.txt")
    path, dist = djikstras(adjacency_matrix, start, end)
    print(pathString(path, start, end))
    print("Cost: " + str(dist))


def djikstras(adjacency_matrix, source_node, destination_node):
    distances = {}
    path = {}
    for node in range(len(adjacency_matrix)):
        distances[node] = float(sys.maxsize)
        path[node] = None
    distances[source_node] = 0

    pq = []
    for node in range(len(adjacency_matrix)):
        heapq.heappush(pq, (node, distances[node]))

    while len(pq) != 0:
        current_node, current_node_distance = heapq.heappop(pq)
        
        for neighbor_node in range(len(adjacency_matrix[current_node])):
            if adjacency_matrix[current_node][neighbor_node] != 0:
                weight = adjacency_matrix[current_node][neighbor_node]
                distance = current_node_distance + weight
                if distance < distances[neighbor_node]:
                    distances[neighbor_node] = distance
                    heapq.heappush(pq, (neighbor_node, distance))
                    path[neighbor_node] = current_node

    return path, distances[destination_node]



if __name__ == "__main__":
    main()
