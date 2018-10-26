class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)
        x = [[0]*n for i in range(n)]
        return x
if __name__ =='__main__':
    solu = Solution()
    piles = [1,2,3]
    x = solu.stoneGame(piles)
    print(x)
