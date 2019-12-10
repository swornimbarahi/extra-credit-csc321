import heapq
import sys

from readAdjacencyMatrix import readAdjacencyMatrix

# print(readAdjacencyMatrix("test_cases/test_case_1.txt"))


def main():
    adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_1.txt")
    printPath(djikstras(adjacency_matrix, start), start, end)
    

def djikstras(graph, starting_vertex):
    distances = {}
    path = {}
    for i in range(len(graph)):    
      distances[i] =  float(sys.maxsize)
      path[i] = None
    distances[starting_vertex] = 0

    pq = []
    for i in range(len(graph)):
      heapq.heappush(pq, (distances[i], i))
      
    while len(pq) != 0:
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor in range(len(graph[current_vertex])):
            if graph[current_vertex][neighbor] != 0:
              weight = graph[current_vertex][neighbor]
              distance = current_distance + weight
              if distance < distances[neighbor]:
                  distances[neighbor] = distance
                  heapq.heappush(pq, (distance, neighbor))
                  path[neighbor] = current_vertex

    return path

def printPath(path, starting_vertex, ending_vertex):
  curr = ending_vertex
  path_list = [curr]
  while(curr != starting_vertex):
    curr = path[curr]
    path_list[:0] = [curr]
  print(path_list)

main()

