#!usr/bin/env python3

"""
  @author:  Swornim Barahi
  @date:    12/10/2019
  @course:  CSC321
  @title:   Extra Credit Project: Dijkstra's Algorithm

  @desc:    The project runs Dijkstra's Algorithm from an input file
            To run the program:
              1.
                You should have python3
              2.
                Create a file with the following format
                  s t
                  d(u0, v0) d(u0, v1) d(u0, v2) ...
                  d(u1, v0) d(u1, v1) d(u1, v2) ...
                  d(u2, v0) d(u2, v1) d(u2, v2) ...
                  .
                  .
                  .
                
                Where s is the starting node and t is the ending node.

                The matrix represents a graph.
                d(ux, vx) is the cost for the edge ux to vx.
                If d(ux, vx) is 0 or 0.0 the edge between ux and vx
                does not exist

              3.
                In the command line, type following command
                python myDijkstra.py <filepath>

                For example:
                python myDijkstra.py test_cases//test_case_0.txt
              

"""


# Importing Priority Queue and sys libraries
import heapq
import sys

# importing utils to help read files and print the path
from utils import readAdjacencyMatrix, pathString


"""
  Command Line Support for Dijkstra's Algorithm
"""
def main():
    adjacencyMatrix, start, end = readAdjacencyMatrix(
        sys.argv[1])
    path, dist = djikstras(adjacencyMatrix, start, end)
    print(pathString(path, start, end))
    print("Cost: " + str(dist))



"""
  The function calculates the shortest path from source to
  destination using dijkstra's algorithm

  For the Priority Queue, I am using the heapq library.
  This library allows me to use a list as a Priority Queue.
  The runtime for changeKey, addKey using this PQ is log(n).
  You can the documentation for this library using the following
  link.
  https://docs.python.org/3/library/heapq.html

  @param  adjacencyMatrix : list[list]
            matrix representation of the weighted directed graph
  @param  sourceNode : int
            starting node in the graph
  @param  destinationNode : int
            destination node in the graph
  
  @returns  path : dict (node, prevNode)
              the shortest path from source to destination
  @returns  dist : float
              the cost of the shortest path
"""
def djikstras(adjacencyMatrix, sourceNode, destinationNode):
    distances = {}
    path = {}
    
    # Initializing an empty Priority Queue
    pq = []
    
    # For every vertex...
    for node in range(len(adjacencyMatrix)):
        # Set the tentative distance to infinity
        distances[node] = float(sys.maxsize)
        # And set the prev node to None
        path[node] = None
    
    # The tentative distance to the source from the source is 0
    distances[sourceNode] = 0

    # For every vertex...
    for node in range(len(adjacencyMatrix)):
        # Insert the nodes and their respective tentative distance
        heapq.heappush(pq, (node, distances[node]))

    # while the priority queue is not empty
    while len(pq) != 0:
        # Pop/Fetch the minimum distance entry from the Priority Queue
        current_node, current_node_distance = heapq.heappop(pq)
        
        # For each node leaving the current node
        for neighbor_node in range(len(adjacencyMatrix[current_node])):
            # If an edge exists leaving the current node
            if adjacencyMatrix[current_node][neighbor_node] != 0:
                # The distance from the current node to the neighbor
                weight = adjacencyMatrix[current_node][neighbor_node]
                # The distance from the source to the neighbor
                distance = current_node_distance + weight
                # If the new distance from source is less than the 
                # tentative distance then...
                if distance < distances[neighbor_node]:
                    # Update the tentative distqance 
                    distances[neighbor_node] = distance
                    # Add the new distance to the Priority Queue
                    heapq.heappush(pq, (neighbor_node, distance))
                    # Record the cheapest way to get to this neighbor
                    path[neighbor_node] = current_node
    return path, distances[destinationNode]



if __name__ == "__main__":
    main()
