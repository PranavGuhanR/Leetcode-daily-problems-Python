class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][j]=2**31
        for i in range(len(matrix)):
            f=0
            for j in range(len(matrix[0])):
                if matrix[i][j]==2**31:
                    f=1
                    break
            if f:        
                for j in range(len(matrix[0])):
                    if matrix[i][j]!=2**31:
                        matrix[i][j]=0                  
        for j in range(len(matrix[0])):
            f=0
            for i in range(len(matrix)):
                if matrix[i][j]==2**31:
                    f=1
                    break
            if f:        
                for i in range(len(matrix)):
                    if matrix[i][j]!=2**31:
                        matrix[i][j]=0 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==2**31:
                    matrix[i][j]=0
        return matrix                               