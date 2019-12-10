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
