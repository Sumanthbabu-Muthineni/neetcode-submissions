class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue
                row_tuple=("row",i,num)
                col_tuple=("col",j,num)
                box_key=("box",i//3,j//3,num)
                if row_tuple in seen or col_tuple in seen or box_key in seen :
                    return False
                seen.add(row_tuple)
                seen.add(box_key)
                seen.add(col_tuple)
        return True

        