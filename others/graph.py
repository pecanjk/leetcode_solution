'''
python graph
	A -> B
	A -> C
	A -> D
	B -> E
	C -> D
	C -> F
	D -> B
	D -> E
	D -> G
	F -> D
	F -> G
	G -> E
'''
#find one path
def findPath(graph,start,end,path=[]):
	path=path+[start]

	if start==end:
		return path
	
	if start not in graph:
		return None
	
	for node in graph[start]:
		if node not in path:
			newpath=findPath(graph,node,end,path)
			if newpath:#valid path
				return newpath
	return None

#find all path
def findAllPaths(graph,start,end,path=[]):
	path=path+[start]
	if start==end:
		print('path ',path)
		return [path]
	
	if start not in graph:
		return []
	
	all_paths=[]
	for node in graph[start]:
		print('node',node)
		if node not in path:
			newpaths=findAllPaths(graph,node,end,path)
			print('newpaths ',newpaths)
			for newpath in newpaths:
				all_paths.append(newpath)

	return all_paths


def findShortestPath(graph,start,end,path=[]):
	path=path+[start]#can not use path+=[start]
	if start==end:
		return path
	
	if start not in graph:
		return None

	shortest_path=None
	for node in graph[start]:
		if node not in path:
			newpath=findShortestPath(graph,node,end,path)
			if newpath:
				if not shortest_path or len(shortest_path)>len(newpath):
					shortest_path=newpath
	
	return shortest_path	

if __name__=="__main__":
	Graph = {'A':  ['B', 'C', 'D'],						# 构建图
		       'B':  ['E'],
	         'C':  ['D', 'F'],
	         'D':  ['B', 'E', 'G'],
	         #'E':  [],
					 'F':  ['D', 'G'],
	         'G':  ['E']}
	out=findPath(Graph,'A','E')
	print('find one path A->E',out)

	out=findAllPaths(Graph,'A','E')
	print('find all paths A->E',out)

	out=findShortestPath(Graph,'A','E')
	print('find shortest path A->E',out)
