class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxArea=0
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                return 0
            
            grid[r][c]=0
            
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
            
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    area=dfs(r,c)
                    maxArea=max(maxArea,area)
        return maxArea
        


        