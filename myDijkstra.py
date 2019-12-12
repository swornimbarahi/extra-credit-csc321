import heapq
import sys

from readAdjacencyMatrix import readAdjacencyMatrix


def main():
    adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_1.txt")
    path, dist = djikstras(adjacency_matrix, start, end)
    printPath(path, start, end)
    print("Cost: " + str(dist))


def djikstras(graph, source_node, destination_node):
    distances = {}
    path = {}
    for node in range(len(graph)):
        distances[node] = float(sys.maxsize)
        path[node] = None
    distances[source_node] = 0

    pq = []
    for node in range(len(graph)):
        heapq.heappush(pq, (node, distances[node]))

    while len(pq) != 0:
        current_node, current_node_distance = heapq.heappop(pq)
        
        for neighbor_node in range(len(graph[current_node])):
            if graph[current_node][neighbor_node] != 0:
                weight = graph[current_node][neighbor_node]
                distance = current_node_distance + weight
                if distance < distances[neighbor_node]:
                    distances[neighbor_node] = distance
                    heapq.heappush(pq, (neighbor_node, distance))
                    path[neighbor_node] = current_node

    return path, distances[destination_node]


def printPath(path, starting_vertex, ending_vertex):
    curr = ending_vertex
    path_list = [curr]
    while(curr != starting_vertex):
        curr = path[curr]
        path_list[:0] = [curr]
    s = ""
    for i in range(len(path_list)):
        s += str(path_list[i]) + "-" if i < len(path_list) - 1 else str(path_list[i])
    print(s)

if __name__ == "__main__":
    main()
