class Solution(object):
    def distributeCandies(self, candies):
        return min(len(set(candies)), len(candies)/2)
