class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        max_Area=0
        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col]==1:
                    stack=[(row,col)]
                    grid[row][col]=0
                    
                    area=0
                    while stack :
                        r,c=stack.pop()
                        area+=1
                        directions=[(0,1),(1,0),(0,-1),(-1,0)]
                        for dr,dc in directions:
                            nr=r+dr
                            nc=c+dc
                            if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1):
                                
                                grid[nr][nc]=0
                                
                                stack.append((nr,nc))
                    max_Area=max(area,max_Area)
        return max_Area


        