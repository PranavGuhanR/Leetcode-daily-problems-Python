class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[set() for i in range(9)]
        c=[set() for i in range(9)]
        b=[[set() for i in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                e=board[i][j]
                
                if e!='.' and ((e in r[i]) or (e in c[j]) or (e in b[i//3][j//3])):
                    return False
                r[i].add(e)
                c[j].add(e)
                b[i//3][j//3].add(e)
        return True            