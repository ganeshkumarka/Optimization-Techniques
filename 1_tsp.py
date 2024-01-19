def travelling_salesman_problem(graph, s):
    vertex = [i for i in range(len(graph)) if i != s]
    min_path = float('inf')
    while True:
        current_pathweight = 0
        k = s
        for i in vertex:
            current_pathweight += graph[k][i]
            k = i
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
        j = len(vertex) - 1
        while j >= 0 and vertex[j] >= vertex[j-1]:
            j -= 1
        if j == 0:
            break
        l = len(vertex) - 1
        while vertex[l] <= vertex[j-1]:
            l -= 1
        vertex[j-1], vertex[l] = vertex[l], vertex[j-1]
        vertex[j:] = vertex[j:][::-1]
    return min_path

if __name__ == "__main__":
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    s = 0
    print("Shortest path ditance: ",travelling_salesman_problem(graph, s))
