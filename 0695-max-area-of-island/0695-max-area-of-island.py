class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        neibs = [[1,0],[-1,0],[0,-1],[0,1]]
        islands, count = Counter(), 0
        
        def dfs(t, i, j):
            if not 0<=i<m or not 0<=j<n or grid[i][j] != 1: return
            islands[t] += 1
            grid[i][j] = '#'
            for x, y in neibs: dfs(t, x+i, y+j)
        
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                dfs(count, i, j)
                count += 1
                
        return max(list(islands.values()) + [0])