class Solution(object):
	def subdomainVisits(self, cpdomains):
		dic = {}
		for line in cpdomains:
			times, url = line.split()
			if url not in dic:
				dic[url] = int(times)
			else:
				dic[url] += int(times)
			while True:
				position = url.find('.')
				if position > 0:
					url = url[position + 1:]
					if url not in dic:
						dic[url] = int(times)
					else:
						dic[url] += int(times)
				else:
					break

		result = []
		for k, v in dic.items():
			result.append(str(v) + " " + k)
		return result

if __name__ == '__main__':
	input = ["9001 discuss.leetcode.com"]
	solu = Solution()
	x = solu.subdomainVisits(input)
	print(x)