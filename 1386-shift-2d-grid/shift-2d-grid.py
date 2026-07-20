class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(m):
            ans=[[0]*len(m[0]) for i in range(len(m))]
            for i in range(len(m)):
                for j in range(1,len(m[0])):
                    ans[i][j]=m[i][j-1]
            ans[0][0]=m[len(m)-1][len(m[0])-1]
            for i in range(1,len(m)):
                ans[i][0]=m[i-1][len(m[0])-1]   
            return ans
        for i in range(k):
            grid=shift(grid)
        return grid                  