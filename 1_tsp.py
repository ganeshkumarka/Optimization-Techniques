from itertools import permutations
from sys import maxsize

V = 4

def travelling_salesman_problem(graph, n):


    nodes = []

    for i in range(V):
        if i != n:
            nodes.append(i)

    minimumPath = maxsize


    nextPermutation = permutations(nodes)


    for i in nextPermutation:

        currentPathWeight = 0
        k = n

        for j in i:
            currentPathWeight += graph[k][j]
            k = j
        currentPathWeight += graph[k][n]
        minimumPath = min(minimumPath, currentPathWeight)

    return minimumPath

if __name__ == "__main__":

    graph = [
        [ 0, 12, 18, 24 ],
        [ 12, 0, 36, 28 ],
        [ 18, 36, 0, 32 ],
        [ 24, 28, 32, 0 ]
    ]

    n = 0

    minimumPathWeight = travelling_salesman_problem(graph, n)
    print("Minimum Cost :", minimumPathWeight)