# DFS: Depth First Search

class Graph:
	'''
	Basic Graph Class
	'''

	def __init__(self, num_vertex):
		self.graph = [[False for j in range(num_vertex)] 
							 for i in range(num_vertex)]
		self.num_vertex = num_vertex

	def addEdge(self, u, v, mode='undirected'):
		self.graph[u][v] = True
		
		if mode=='undirected':
			self.graph[v][u] = True

	def dfs_util(self, v, visited):
		# Set the current node as visited
		visited[v] = True

		# Print the current vertex
		print(v, end = ' ')

		# Recur for all its adjacent neighbours
		for neighbour_idx in range(self.num_vertex):
			# If a neighbour is not visited then visit it.
			if self.graph[v][neighbour_idx] and not visited[neighbour_idx]:
				self.dfs_util(neighbour_idx, visited)

	def dfs(self, v):
		visited = [False for _ in range(self.num_vertex)]

		self.dfs_util(v, visited)
		print()

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(2)

# Output: 2, 0, 1, 3
