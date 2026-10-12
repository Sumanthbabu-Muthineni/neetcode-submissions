class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    islands+=1
                    grid[row][col]="0"
                    stack=[(row,col)]
                    while stack :
                        row,col=stack.pop()
                        directions=[
                            (-1,0),
                            (0,1),
                            (1,0),
                            (0,-1)
                        ]
                        for dr,dc in directions:
                            nr=row+dr
                            nd=col+dc

                            if  0<=nr<rows and 0<=nd<cols and grid[nr][nd]=="1":
                                grid[nr][nd]="0"
                                stack.append((nr,nd))
        return islands










