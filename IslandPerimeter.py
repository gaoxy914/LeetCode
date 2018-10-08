class Solution(object):
    def islandPerimeter(self, grid):
        length = len(grid)-1
        width = len(grid[0])-1
        for line in grid:
            line.insert(0, 0)
            line.append(0)
        grid.insert(0, [0]*(width+3))
        grid.append([0]*(width+3))
        def perimeter(x, y):
            p = 0
            if not grid[x][y-1]:
                p += 1
            if not grid[x][y+1]:
                p += 1
            if not grid[x-1][y]:
                p += 1
            if not grid[x+1][y]:
                p += 1
            return p
        result = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[1])-1):
                if grid[i][j]:
                    result += perimeter(i, j)
        return result


if __name__ == '__main__':
    grid = [[1],[0],[0]]
    solu = Solution()
    x = solu.islandPerimeter(grid)
    print(x)