#!usr/bin/env python3

def readAdjacencyMatrix(filepath):
    matrixFile = list(open(filepath, "r"))
    matrix = []
    for i in range(1, len(list(matrixFile))):
        line = []
        for distance in matrixFile[i].strip().split(' '):
            line.append(float(distance))
        matrix.append(line)
    start = int(matrixFile[0].strip().split(' ')[0])
    end = int(matrixFile[0].strip().split(' ')[1])
    return matrix, start, end

def pathString(path, starting_vertex, ending_vertex):
    curr = ending_vertex
    path_list = [curr]
    while(curr != starting_vertex):
        curr = path[curr]
        path_list[:0] = [curr]
    s = ""
    for i in range(len(path_list)):
        s += str(path_list[i]) + "-" if i < len(path_list) - 1 else str(path_list[i])
    return s
