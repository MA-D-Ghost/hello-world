'''
Ho ten: Ton Thien Minh Anh
MSSV: 18110049
Bai thuc hanh Nhap Mon AI tuan 01
'''

# IMPORT THU VIEN
import queue as Q
from operator import itemgetter, attrgetter
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
			return True
		else:
			return False
			
	def print_graph(self):
		for key in list(self.vertices.keys()): 
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

	def ucs(self, start, end):
		queue = Q.PriorityQueue()
		queue.put((0, [start]))
    
		while not queue.empty():
			node = queue.get()
			current = node[1][len(node[1]) - 1]
        
			if end in node[1]:
				print("Duong di theo thuat toan UCS la: " + str(node[1]) + ", Cost = " + str(node[0]))
				break
        
			cost = node[0]
			if len(self.vertices[current].neighbors) == 0:
				cost = cost
			elif len(self.vertices[current].neighbors) ==1:
				cost = cost + self.vertices[current].neighbors[0][1]
			else: 
				min = self.vertices[current].neighbors[0][1]
				for i in range(len(self.vertices[current].neighbors)):
					if self.vertices[current].neighbors[i][1] < min:
						min = self.vertices[current].neighbors[i][1]
				cost = cost + min #cost + self.vertices[current].neighbors[i][1]
			for key in list(self.vertices.keys()):
				if key in str(self.vertices[current].neighbors):
					temp = node[1][:]
					temp.append(key)
					queue.put((cost , temp))
	

print("0. Thuat toan BFS & DFS")
print("1. Thuat toan UCS")
k = input("Nhap file Input ban muon: ")
k = int(k)
if k==0:
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

	#g.print_graph()
	print('Duong di theo thuat toan BFS la:')
	print(g.bfs('V0','V17'))

	print('Duong di theo thuat toan DFS la:')
	print(g.dfs('V0','V17'))

elif k ==1:
	# ============= FILE INPUT CHO UCS ==========

	path = '/home/ton-anh/Nhap Mon AI/Tuan01/InputUCS.txt'
	f2 = open(path,"r")

	# Input so phan tu cua Graph
	a = int(f2.readline())

	# Input start va goal cua thuat toan tim kiem
	b = f2.readline()
	start,goal = b.split(' ')
	start = int(start)
	goal = int(goal)

	# Tao vertex cua Graph
	h = Graph()
	for i in range(a):
		i ='V' + str(i)
		h.add_vertex(Vertex(i))

	# # Tao edge cua Graph
	for i in range(a):
		temp = f2.readline()
		matrix = []
		matrix = temp.split(' ')
		for j in range(a):
			v1 = 'V'+str(i)
			v2 = 'V'+str(j)
			temp2 = int(matrix[j])
			if (temp2 != 0):
				h.add_edge(v1,v2,temp2)

	#h.print_graph()
	h.ucs('V0','V17')
else:
	print("So ban nhap vao khong hop le!")
