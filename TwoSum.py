class Solution(object):
	def twoSum(self, nums, target):
		dict = {}
		for i in range(len(nums)):
			if target - nums[i] in dict:
				return (dict[target-nums[i]], i)
			dict[nums[i]] = i

if __name__ == '__main__':
	nums = [3, 2, 4]
	target = 6
	solu = Solution()
	x = solu.twoSum(nums, target)
	print x