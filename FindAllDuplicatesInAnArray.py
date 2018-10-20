class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                result.append(abs(i))
            nums[index] = -nums[index]
        return result
