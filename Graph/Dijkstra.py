import heapq

class Dijkstra:
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
        print()

    def apply_dijkstra(self, src, dst):

        priority_queue = []
        for (u, w) in self.G[src]:
            priority_queue.append((w, src, u))

        heapq.heapify(priority_queue)

        cost = [float('inf') for _ in range(self.V)]
        cost[src] = 0
        path = [-1 for _ in range(self.V)]

        while priority_queue:

            value, from_, to_ = heapq.heappop(priority_queue)

            # Relaxation Step
            if cost[to_] > cost[from_] + value:
                cost[to_] = cost[from_] + value
                path[to_] = from_

            for (u, w) in self.G[to_]:
                heapq.heappush(priority_queue, (w, to_, u))

        # Extracting followed path
        node = dst
        res_path = []

        while node != src:
            res_path.append(node)
            node = path[node]

        res_path.append(src)
        return {'cost': cost,
        'path': res_path[::-1]
        }


sp = Dijkstra(6, 8)
sp.add_edge(0, 1, 2)
sp.add_edge(0, 2, 4)
sp.add_edge(1, 2, 1)
sp.add_edge(1, 3, 7)
sp.add_edge(2, 4, 3)
sp.add_edge(4, 3, 2)
sp.add_edge(3, 5, 1)
sp.add_edge(4, 5, 5)

sp.print_graph()


res = sp.apply_dijkstra(0, 5)
print("cost: ", res['cost'])
print("path:", res['path'])

#  Returns:
# |0| -> (1, 2) -> (2, 4)
# |1| -> (2, 1) -> (3, 7)
# |2| -> (4, 3)
# |3| -> (5, 1)
# |4| -> (3, 2) -> (5, 5)
# |5| -> _

# cost:  [0, 2, 3, 8, 6, 9]
# path: [0, 1, 2, 4, 3, 5]
