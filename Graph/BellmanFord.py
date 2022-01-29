class shortestPath:
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

    def bellman_ford(self, src, dst):
        '''
        Bellman Ford Algorithm:
            - Single source shortest path algorithm.
            - Dijkstra's Shortest Path algorithm is incapable of solving for negative
            edges. Bellman-Ford algorithm achieves to find shortest path with an additional
            complexity.

        Drawback:
            - When there is a negative cycle in the graph, as in the other shortest path algorithms
            Bellman-Ford algorithm also fails.

        Approach:
            - Let shortest path between nodes u and v be denoted as p(u, v). Then, if there are |V|
            nodes in the graph, p(u, v) has maximum |V| - 1 edges: <E_1, E_2, ..., E_n-1>
            - That means, in total of |V| - 1 iterations if we relax all of the edges in the graph, we
            can get p(u, v).

        Complexity:
            - Observe that, Bellman-Ford algorithm iterates over |V| - 1 times over entire edges of |E|.
            Complexity is O(|E||V|). If given graph is a complete (dense), suppose there are n nodes, then total
            of n * (n - 1) / 2 edges. This makes complexity even worse: O(n^3).
        '''
        cost = [[float('inf') for i in range(self.V)] for j in range(self.V)]
        cost[src][src] = 0

        for k in range(self.E - 1):
            for v in range(self.V):
                # Relaxation part
                for (j, w) in self.G[v]:
                    if cost[src][j] > cost[src][v] + w:
                        cost[src][j] = cost[src][v] + w


        return cost[src][dst]


sp = shortestPath(7, 10)
sp.add_edge(0, 1, 6)
sp.add_edge(0, 2, 5)
sp.add_edge(0, 3, 5)
sp.add_edge(1, 4, -1)
sp.add_edge(2, 1, -2)
sp.add_edge(2, 4, 1)
sp.add_edge(3, 2, -2)
sp.add_edge(3, 5, -1)
sp.add_edge(4, 6, 3)
sp.add_edge(5, 6, 3)


sp.print_graph()
src = 0
dst = 6
print(f"Minimum cost between {src} and {dst}: {sp.bellman_ford(src, dst)}")
