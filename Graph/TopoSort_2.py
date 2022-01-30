class TopoSort:
    def __init__(self, V):
        '''
        Args:
            V: total number of nodes.
            E: total number of edges.
        Assumption:
            Graph is directed acyclic graph.
        '''

        # Graph parameters
        self.V = V


        # Initialize graph: Adjacency List
        self.G = {i : [] for i in range(V)}

    def addEdge(self, from_, to_):
        self.G[from_].append(to_)


    def print_graph(self):
        for i in range(self.V):
            print(f"|{i}| ->", end=' ')
            t = len(self.G[i])
            for j in range(t - 1):
                print(f"{self.G[i][j]} ->", end=' ')
            print(self.G[i][-1] if t else '_')
        print()


    def topo_utility_dfs(self, node, stack, visited):
        visited[node] = True

        for u in self.G[node]:
            if not visited[u]:
                self.topo_utility_dfs(u, stack, visited)

        stack.append(node)

    def apply_topo_sort(self):

        stack = []
        visited = [False] * self.V

        for v in self.G:
            if not visited[v]:
                self.topo_utility_dfs(v, stack, visited)

        print(*stack[::-1])

g = TopoSort(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.print_graph()
g.apply_topo_sort()

# Output: 5 4 2 3 1 0
