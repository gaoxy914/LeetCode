class Solution(object):
	def allPathsSourceTarget(self, graph):
		def findPath(graph, start, end):
			paths = []
			for node in graph[start]:
				if node == end:
					path = [start, end]
					paths.append(path)
				else:
					temp = findPath(graph, node, end)
					for path in temp:
						path.insert(0, start)
						paths.append(path)
			return paths
		return findPath(graph, 0, len(graph)-1)


if __name__ == '__main__':
	solu = Solution()
	A = [[1,2], [3], [3], []]
	x = solu.allPathsSourceTarget(A)
	print(x)