# Breadth First Search
from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def bfs(self, v):

		# Create a visited list
		visited = [False] * (max(self.graph) + 1)

		queue = [v]
		visited[v] = True
		while queue:
			node = queue.pop(0)
			print(node, end = ' ')

			# iterate for neighbours
			for neighbour in self.graph[node]:
				if not visited[neighbour]:
					visited[neighbour] = True
					queue.append(neighbour)

		print()


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs(2)

# Output: 2 0 3 1
