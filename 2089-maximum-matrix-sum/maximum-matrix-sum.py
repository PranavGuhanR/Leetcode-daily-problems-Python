class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n=f=0
        sum=0
        smallest=abs(matrix[0][0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    f=1
                sum+=abs(matrix[i][j])
                smallest=min(smallest,abs(matrix[i][j]))
                if matrix[i][j]<0:
                    n+=1
        if (n%2) and (f==0) :
            return sum-(2*smallest)    
        return sum                        