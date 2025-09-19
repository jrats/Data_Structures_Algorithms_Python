inf = 9999

def printSolution(v, distance):
    for i in range(v):
        for j in range(v):
            if distance[i][j] == inf:
                print('INF', end=" ")
            else:
                print(distance[i][j], end=' ')
        print(" ")

def floydWarshall(v, G):
    distance = G
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    printSolution(v, distance)


G = [[0, 8, inf, 1],
     [inf, 0, 1, inf],
     [4, inf, 0, inf],
     [inf, 2, 9, 1]]

floydWarshall(4, G)




