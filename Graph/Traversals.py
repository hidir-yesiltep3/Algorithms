from collections import deque

class Traversal:
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


    def BFS(self, src):
        queue = deque()

        queue.append(src)
        visited = [False] * self.V
        visited[src] = True
        while queue:
            node = queue.popleft()
            print(node, end = ' ')

            for v in self.G[node]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

    def DFS_utility(self, node, visited):
        print(node, end = ' ')
        visited[node] = True

        for v in self.G[node]:
            if not visited[v]:
                self.DFS_utility(v, visited)

    def DFS_recursive(self, src):
        visited = [False] * self.V

        self.DFS_utility(src, visited)

    def DFS_iterative(self, src):
        stack = [src]
        visited = [False] * self.V

        while stack:
            node = stack.pop()
            visited[node] = True

            print(node, end = ' ')

            for v in self.G[node]:
                if not visited[v]:
                    stack.append(v)

g = Traversal(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.print_graph()
g.BFS(2)
# Output: 2 0 3 1
print()
g.DFS_recursive(2)
# Output: 2 0 1 3
print()
print()
g = Traversal(5); # Total 5 vertices in graph
g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(2, 1);
g.addEdge(0, 3);
g.addEdge(1, 4);
g.print_graph()
g.DFS_iterative(0)
