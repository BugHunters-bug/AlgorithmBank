from termcolor import colored
INF = float("inf")
NE = -float("inf")

def BellmanFord(vertices: list, edgesWeights: list, source: tuple) -> tuple[list, list]:
    distance = dict()
    predecessor = dict()

    for v in vertices:
        distance[v] = INF             # Initialize the distance to all vertices to infinity
        predecessor[v] = NE         # And having a null predecessor
    
    distance[source] = 0

    for _ in range(len(vertices) - 1):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if edgesWeights[i][j] == NE:
                    continue
                if distance[i] + edgesWeights[i][j] < distance[j]:
                    distance[j] = distance[i] + edgesWeights[i][j]
                    predecessor[j] = i
    
    print("\n\nVertices:\tA\tB\tC\tD\tE\n\n")
    print("Distances:", end="\t")
    for i in range(len(vertices)):
        print(distance[i],end="\t")
    
    print("\nPredecessor:", end="\t")
    for i in range(len(vertices)):
        if predecessor[i] == NE:
            print("NA", end="\t")
            continue
        
        print(predecessor[i], end="\t")

if __name__ == "__main__":
    number_of_nodes = 5
    vertices = [i for i in range(5)]
    edgesWeights = [
        [0, -1, 4, NE, NE],
        [NE, 0, 3, 2, 2],
        [NE, NE, NE, NE, NE],
        [NE, 1, 5, 0, NE],
        [NE, NE, NE, -3, 0]
    ]

    BellmanFord(vertices, edgesWeights, 0)