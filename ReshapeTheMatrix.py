class Solution(object):
    def matrixReshape(self, nums, r, c):
        m = len(nums)
        n = len(nums[0])
        if r*c != m*n:
            return nums
        result = [([0]*c) for i in range(r)]
        x = 0
        y = 0
        for i in range(r):
            for j in range(c):
                if y == n:
                    x += 1
                    y = 0    
                result[i][j] = nums[x][y]
                y += 1
        return result
