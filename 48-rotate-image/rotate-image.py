class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n=len(matrix)

        def rotv(x,y):
            t=matrix[x][y]
            t,matrix[y][n-x-1]=matrix[y][n-x-1],t
            t,matrix[n-x-1][n-y-1]=matrix[n-x-1][n-y-1],t
            t,matrix[n-y-1][x]=matrix[n-y-1][x],t
            matrix[x][y]=t

        for i in range(n//2):
            for j in range(n//2+n%2):
                rotv(i,j)

        return matrix                             