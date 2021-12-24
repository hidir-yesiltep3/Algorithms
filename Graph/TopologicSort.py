# Topologic Sort implementation 
from collections import defaultdict

class Graph:
	def __init__(self, num_vertices):
		# This class represents graphs as in the
		# adjacency list form.
		self.graph = defaultdict(list)
		
		# Total number of vertices
		self.V = num_vertices


	def addEdge(self, u, v):
		self.graph[u].append(v)


	def topologicSortUtil(self, i, visited, stack):
		# Mark the current vertex as visited
		visited[i] = True

		# Visit all its neighbour vertices.
		for j in self.graph[i]:
			if not visited[j]:
				self.topologicSortUtil(j, visited, stack)

		# After all of the neighbours are visited, push it into
		# stack.
		stack.append(i)


	def topologicSort(self):
		# Mark all the vertices as unvisited.
		visited = [False] * self.V

		stack = []

		# Recur for all vertices
		for i in range(self.V):
			if not visited[i]:
				self.topologicSortUtil(i, visited, stack)

		print(stack[::-1])



g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicSort()
