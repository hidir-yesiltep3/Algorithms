# Kosaraju's Algorithm
from collections import defaultdict

class Graph:
	def __init__(self, num_vertices):
		self.graph = defaultdict(list)
		self.V = num_vertices


	def addEdge(self, u, v):
		self.graph[u].append(v)


	def DFS_Util(self, v, visited):
		visited[v] = True
		print(v, end= ' ')

		for neighbour in self.graph[v]:
			if not visited[neighbour]:
				self.DFS_Util(neighbour, visited)

	def fill_order(self, v, visited, stack):
		visited[v] = True

		for i in self.graph[v]:
			if not visited[i]:
				self.fill_order(i, visited, stack)


		stack.append(v)


	def getTranspose(self):
		# Create a new graph and take the current graph's transpose.
		g = Graph(self.V)

		# Recur for all of the vertices
		for i in self.graph:
			# Recur for all of its neighbours
			for j in self.graph[i]:
				g.addEdge(j, i)

		return g


	# Main function which finds the all of the strongly connected components based
	# on finishing time.
	def get_SCC(self):

		stack = []

		visited = [False] * self.V

		# Fill the stack based on finishing time of their DFS.
		for i in range(self.V):
			if not visited[i]:
				self.fill_order(i, visited, stack)
		

		# Now stack is filled. Take the transpose of the graph
		# and traverse it with dfs again.

		visited = [False] * self.V

		# Get the transposed graph
		gT = self.getTranspose()

		while stack:
			vertex = stack.pop()
			if not visited[vertex]:
				gT.DFS_Util(vertex, visited)
				print()

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.get_SCC()

