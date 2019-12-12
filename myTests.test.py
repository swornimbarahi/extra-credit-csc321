#!usr/bin/env python3
import unittest

from utils import readAdjacencyMatrix, pathString
from myDijkstra import djikstras

class TestDijkstra(unittest.TestCase):

    def test_0(self):
        adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_0.txt")
        path, dist = djikstras(adjacency_matrix, start, end)
        self.assertEqual(pathString(path, start, end), "0-3-2")
        self.assertAlmostEqual(dist, 8.2)
        self.assertNotEqual(dist, 8)
    
    def test_1(self):
        adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_1.txt")
        path, dist = djikstras(adjacency_matrix, start, end)
        self.assertEqual(pathString(path, start, end), "2-3-0-9")
        self.assertAlmostEqual(dist, 10.0)
        self.assertNotEqual(dist, 11.0)

    def test_2(self):
        adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_2.txt")
        path, dist = djikstras(adjacency_matrix, start, end)
        self.assertEqual(pathString(path, start, end), "25-14-2-9-4-3")
        self.assertAlmostEqual(dist, 11.2)
        self.assertNotEqual(dist, 11.0)


    def test_3(self):
        adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_3.txt")
        path, dist = djikstras(adjacency_matrix, start, end)
        self.assertEqual(pathString(path, start, end), "7-16-19")
        self.assertAlmostEqual(dist, 1.6)
        self.assertNotEqual(dist, 2)

    def test_4(self):
        adjacency_matrix, start, end = readAdjacencyMatrix(
        "test_cases/test_case_4.txt")
        path, dist = djikstras(adjacency_matrix, start, end)
        self.assertEqual(pathString(path, start, end), "33-18-27-13-1")
        self.assertAlmostEqual(dist, 1.9)
        self.assertNotEqual(dist, 2)


if __name__ == '__main__':
    unittest.main()