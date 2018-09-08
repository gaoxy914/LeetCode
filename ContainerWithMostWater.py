class Solution(object):
	def maxArea(self, height):
		left = 0
		right = len(height)-1
		maxArea = 0
		while left != right:
			maxArea = max(maxArea, min(height[left], height[right])*(right-left))
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1
		return maxArea

if __name__ == '__main__':
	print Solution().maxArea([1, 2, 3])			