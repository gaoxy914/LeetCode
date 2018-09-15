class Solution(object):
	def arrayPairSum(self, nums):
		nums.sort()
		sum = 0
		for i in range(len(nums) / 2):
			sum += nums[2*i]
		return sum