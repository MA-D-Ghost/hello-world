'''
Ho ten: Ton Thien Minh Anh
MSSV: 18110049
Bai thuc hanh Nhap Mon AI tuan 01
'''

# IMPORT THU VIEN
#from queue import Queue,PriorityQueue
import queue as Q
# CLASS VERTEX
class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def add_neighbor(self, v, weight):
		if v not in self.neighbors:
			self.neighbors.append((v, weight))
			self.neighbors.sort()

# CLASS GRAPH
class Graph:
	vertices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v, weight):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_neighbor(v, weight)
			#self.vertices[v].add_neighbor(u, weight)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in list(self.vertices.keys()): #sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))

	def bfs(self, start, goal):
    	# maintain a queue of paths
		queue = []
		# push the first path into the queue
		queue.append([start])
		while queue:
			# get the first path from the queue
			path = queue.pop(0)
			# get the last node from the path
			vertex = path[-1]
			# path found
			if vertex == goal:
				return path
			# enumerate all adjacent nodes, construct a new path and push it into the queue
			for key in list(self.vertices.keys()):
				if key in str(self.vertices[vertex].neighbors):
					new_path = list(path)
					new_path.append(key)
					queue.append(new_path)

	def dfs(self, start, goal):
		stack = [(start, [start])]
		visited = set()
		while stack:
			(vertex, path) = stack.pop()
			if vertex not in visited:
				if vertex == goal:
					return path
				visited.add(vertex)
				for key in list(self.vertices.keys()):
					if key in str(self.vertices[vertex].neighbors):
						stack.append((key, path + [key]))
	

	def ucs(self, start, goal):
		queue = PriorityQueue()
		queue.put((0, [start]))

		while not queue.empty():
			vertex = queue.get()
			current = vertex[1][len(vertex[1]) - 1]
				
			if goal in vertex[1]:
				print("Path found: " + str(vertex[1]) + ", Cost = " + str(vertex[0]))
				break
			
			cost = vertex[0]
			for key in list(self.vertices.keys()):
				if key in str(self.vertices[vertex].neighbors):
					temp = vertex[1][:]
					temp.append(key)
					queue.put((cost + int(self.vertices[vertex].neighbors[key]), temp))

	def search(self, start, goal):
		queue = Q.PriorityQueue()
		queue.put((0, [start]))
    
		while not queue.empty():
			node = queue.get()
			current = node[1][len(node[1]) - 1]
        
			if goal == node[1]:
				print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
				break
        
			cost = node[0]
			for neighbor in self.vertices[current]:
				temp = node[1][:]
				temp.append(neighbor)
				queue.put((cost + graph[current][neighbor], temp))


# ======= PHAN CHUONG TRINH ===========
path = '/home/ton-anh/Nhap Mon AI/Tuan01/Input.txt'
f = open(path,"r")

# ============= FILE INPUT CHO BFS VA DFS ==========
# Input so phan tu cua Graph
a = int(f.readline())

# Input start va goal cua thuat toan tim kiem
b = f.readline()
start,goal = b.split(' ')
start = int(start)
goal = int(goal)

# Tao vertex cua Graph
g = Graph()
for i in range(a):
	i ='V' + str(i)
	g.add_vertex(Vertex(i))

# Tao edge cua Graph
for i in range(a):
	temp = f.readline()
	matrix = []
	matrix = temp.split(' ')
	for j in range(a):
		v1 = 'V'+str(i)
		v2 = 'V'+str(j)
		temp2 = int(matrix[j])
		if (temp2 ==1):
			g.add_edge(v1,v2,0)

g.print_graph()
#print(g.bfs2('V0','V17'))
#print(len(g.vertices['V0'].neighbors))
#print(g.vertices['V0'].neighbors[2])
#print(list(g.vertices['V0'].neighbors))
print('Duong di theo thuat toan BFS la:')
print(g.bfs('V0','V17'))

# print('Duong di theo thuat toan DFS la:')
# print(g.dfs('V0','V17'))

# ============= FILE INPUT CHO UCS ==========

path = '/home/ton-anh/Nhap Mon AI/Tuan01/InputUCS.txt'
f = open(path,"r")

# Input so phan tu cua Graph
a = int(f.readline())
print(a)

# Input start va goal cua thuat toan tim kiem
b = f.readline()
start,goal = b.split(' ')
start = int(start)
goal = int(goal)

# Tao vertex cua Graph
h = Graph()
for i in range(a):
	i ='V' + str(i)
	h.add_vertex(Vertex(i))

# Tao edge cua Graph
for i in range(a):
	temp = f.readline()
	matrix = []
	matrix = temp.split(' ')
	for j in range(a):
		v1 = 'V'+str(i)
		v2 = 'V'+str(j)
		temp2 = int(matrix[j])
		if (temp2 !=0):
			h.add_edge(v1,v2,temp2)

# h.print_graph()
print(h.search('V0','V17'))