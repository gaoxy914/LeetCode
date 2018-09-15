class Solution(object):
	def peakIndexInMountainArray(self, A):
		def findMax(A, start, end):
			mid = (start + end) // 2
			if A[mid] > A[mid+1] and A[mid] > A[mid-1]:
				return mid
			if A[mid] > A[mid-1] and A[mid] < A[mid+1]:
				return findMax(A, mid+1, end)
			if A[mid] < A[mid-1] and A[mid] > A[mid+1]:
				return findMax(A, start, mid-1)

		return findMax(A, 0, len(A)-1)

if __name__ == '__main__':
	solu = Solution()
	A = [0,2,1,0]
	x = solu.peakIndexInMountainArray(A)
	print(x)