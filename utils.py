#!usr/bin/env python3

"""
  The function reads the input from a file

  @param  filepath
            the relative path of the file to read

  @returns  matrix
              the graph represented by an adjacency matrix
  @returns  start
              the source node for the algorithm
  @returns  end
              the destination node for the algorithm
"""
def readFileToAdjacencyList(filepath):
    matrixFile = list(open(filepath, "r"))
    adjacencyList = {}
    for i in range(1, len(list(matrixFile))):
        line = {}
        lineContent = matrixFile[i].strip().split(' ')
        for idx in range(len(lineContent)):
            if float(lineContent[idx]) != 0.0:
              line[idx] = float(lineContent[idx])
        adjacencyList[i - 1] = line
    start = int(matrixFile[0].strip().split(' ')[0])
    end = int(matrixFile[0].strip().split(' ')[1])
    return adjacencyList, start, end


"""
  The function converts the path dictionary into a string
  @param  path
  @param  startingVertex
            the source node
  @param  endingVertex
            the destination node
  
  @returns  s
              the string representation of the path
"""
def pathString(path, startingVertex, endingVertex):
    curr = endingVertex
    path_list = [curr]
    while(curr != startingVertex):
        curr = path[curr]
        path_list[:0] = [curr]
    s = ""
    for i in range(len(path_list)):
        s += str(path_list[i]) + "-" if i < len(path_list) - 1 else str(path_list[i])
    return s
