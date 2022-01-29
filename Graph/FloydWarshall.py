class allPairsShortestPath:
    def __init__(self, V, E):
        '''
        Args:
            V: total number of nodes.
            E: total number of edges.
        Assumption:
            Graph is directed acyclic graph.
        '''

        # Graph parameters
        self.V = V
        self.E = E

        # Initialize graph: Adjacency List
        self.G = {i : [] for i in range(V)}

    def add_edge(self, from_, to_, weight):
        self.G[from_].append((to_, weight))


    def print_graph(self):
        for i in range(self.V):
            print(f"|{i}| ->", end=' ')
            t = len(self.G[i])
            for j in range(t - 1):
                print(f"{self.G[i][j]} ->", end=' ')
            print(self.G[i][-1] if t else '_')


    def floyd_warshall(self):
        '''
        Floyd Warshall Algorithm:
            - Apart from Dijkstra and Bellman-Ford algorithms (which are single source shortest path algorithms),
        there is also an algorithm called Floyd Warshall in an attempt to find all pairs shortest path.
            - If there are in total |V| this algorithm finds shortest path between
        V_i and V_j where i, j in < 1...V >.

        Approach:
            - Floyd-Warshall computes paths in order of increasing vertice indices.
            - We will hold a cost matrix A_k of |V| x |V|. Here k denotes the intermediate vertice index.
            - We will check if we can obtain shorter path p(u, v) between nodes u and v by adding an intermediate
            node k, i.e p(u, v) ?= p(u, k) + p(k, v).

        Recurrence Relation:
            - Since Floyd-Warshall algorithm makes use of dynamic programming, we can write a recurrence
            relation.
                                #############################################################
                                ## A_k[u][v] = min(A_k-1[u][k] + A_k-1[k][v], A_k-1[u][v]) ##
                                #############################################################

        Complexity:
            Space complexity: O(V^2)
            Time  complexity: O(V^3)
        '''

        # Initializing the cost matrix
        A = [[float("inf") for i in range(self.V)] for j in range(self.V)]

        # Note that, every entry in A_0[u][v] have the value w(u, v) if there is and edge between
        # nodes u and v otherwise it will remain as inf. In addition to that, we are assuming graph
        # there is no path like a -> a (loop). So diagonal etries will be set to 0.

        for v in range(self.V):
            for (u, w) in self.G[v]:
                A[v][u] = w

        for v in range(self.V):
            A[v][v] = 0

        # Now, start from k = 0 to k = |V| and construct the matrix A_k
        for k in range(self.V):
            for v in range(self.V):
                for u in range(self.V):

                    if v == k or u == k:
                        continue
                    if A[v][u] > A[v][k] + A[k][u]:
                        A[v][u] = A[v][k] + A[k][u]

        return A


sp = allPairsShortestPath(4, 7)
sp.add_edge(0, 3, 7)
sp.add_edge(3, 0, 2)
sp.add_edge(0, 1, 3)
sp.add_edge(1, 0, 8)
sp.add_edge(1, 2, 2)
sp.add_edge(2, 3, 1)
sp.add_edge(2, 0, 5)

sp.print_graph()
print()

matrix = sp.floyd_warshall()
for i in matrix:
    print(i)

# Graph: 
# |0| -> (3, 7) -> (1, 3)
# |1| -> (0, 8) -> (2, 2)
# |2| -> (3, 1) -> (0, 5)
# |3| -> (0, 2)

# Matrix:
# [0, 3, 5, 6]
# [5, 0, 2, 3]
# [3, 6, 0, 1]
# [2, 5, 7, 0]
