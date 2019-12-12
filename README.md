# Dijkstra's Algorithm

Dijkstra's Algorithm was the work of a computer scientist named Eddger W. Dijkstra. It is an algorithm that is used to calculate the shortest path between two points on a weighted graph. For more information on Dijkstra's Algorithm, [click here](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

## How to run
1. You should have
2. Create a file with the following format
    ```
        s t
        d(u0, v0) d(u0, v1) d(u0, v2) ...
        d(u1, v0) d(u1, v1) d(u1, v2) ...
        d(u2, v0) d(u2, v1) d(u2, v2) ...
        .
        .
        .
    ```
    Where s is the starting node and t is the ending node. They are indices of the matrix as well.
    If the size of the matrix is n, then `0 < s, t < n`.
    
    The matrix represents a graph and `d(ux, vx)` is the cost for the edge ux to vx.
    If `d(ux, vx)` is 0 or 0.0 the edge between ux and vx does not exist

3. In the command line, type following command
`python myDijkstra.py <filepath>`
For example:
`python myDijkstra.py test_cases//test_case_0.txt`

## How to run My test cases
You can run my test cases with the following command
`python myTests.test.py`