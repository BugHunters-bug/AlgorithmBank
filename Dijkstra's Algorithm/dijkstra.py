import random

def init_block(i, j, m, n):
    if (i == 0 and j == 0) or (i == m-1 and j == n-1):
        return 0
    else:
        if random.random() < 0.3:
            return -1

    return 0

def init_distances(rows, cols):
    Score = {}
    for i in range(rows):
        for j in range(cols):
            Score[(i,j)] = float("inf")

    return Score

def get_neighbours(node, m, n):
    neighbours = []
    i = node[0]
    j = node[1]
    if i-1 > -1:
        neighbours.append((i-1, j)) 
    if i+1 < m:
        neighbours.append((i+1, j)) 
    if j-1 > -1:
        neighbours.append((i, j-1)) 
    if j+1 < n:
        neighbours.append((i, j+1)) 

    return neighbours

def get_lowest_f(Q, distance):
    lowest = float("inf")
    lowestEle = None
    for ele in Q:
        if distance[ele] < lowest:
            lowestEle = ele

    if lowestEle == None:
        return Q[0] 
    return lowestEle

def Dijkstra(grid, start, end, m, n):
    if grid[end[0]][end[1]] == -1 or grid[start[0]][start[1]] == -1: # If end itself is a wall
        return 0, -1

    Q = [(i,j) for i in range(m) for j in range(n)]
    distance = init_distances(m, n)
    predecessor = init_distances(m, n)
    distance[start] = 0

    while len(Q) > 0:
        current = get_lowest_f(Q, distance)
        print(current)
        Q.remove(current)
        for neighbour in get_neighbours(current, m, n):
            if neighbour in Q:
                alt = distance[current] + 1
                if grid[neighbour[0]][neighbour[1]] != -1 and alt < distance[neighbour]: 
                    distance[neighbour] = alt
                    predecessor[neighbour] = current
    
    return distance, predecessor

def display(grid):
    for arr in grid:
        for ele in arr:
            print(ele, end = "\t")
        print()

if __name__ == "__main__":
    m = 4
    n = 4
    grid = [[ init_block(i, j, m, n) for j in range(n)] for i in range(m)]
    print("Graph:")
    display(grid)
    print("\nShortest Route (indices):")
    start = (0,0)
    end = (m-1, n-1)
    route = []
    distance, predecessor = Dijkstra(grid, start, end, m, n)
    node = end
    if predecessor == -1:
        print("No path available.")
    else:
        while node in predecessor:
            route.append(node)
            node = predecessor[node]

    print(route[::-1])
