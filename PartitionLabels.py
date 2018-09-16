class Solution(object):
	def partitionLabels(self, S):
		dic = {}
		for i in range(len(S)-1, -1, -1):
			if len(dic) > 26:
				break
			if S[i] not in dic:
				dic[S[i]] = i
		l = []
		result = []
		for i in range(len(S)):
			if i < dic[S[i]] and S[i] not in l:
				l.append(S[i])
			if i == dic[S[i]] and len(l) > 0:
				if S[i] in l:
					l.remove(S[i])
			if i == dic[S[i]] and len(l) == 0:
				result.append(i+1)
				l = []
		for i in range(len(result)-1, 0, -1):
			result[i] = result[i] - result[i-1]
		return result

if __name__ == '__main__':
	solu = Solution()
	S = "ababcbacadefegdehijhklij"
	x = solu.partitionLabels(S)
	print(x)