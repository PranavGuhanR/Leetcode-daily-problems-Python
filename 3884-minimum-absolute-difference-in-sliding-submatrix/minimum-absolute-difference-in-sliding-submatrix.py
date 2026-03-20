class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def asm(s):
            L=[]
            for i in range(s[0],s[0]+k):
                for j in range(s[1],s[1]+k):
                    if grid[i][j] not in L:
                        L.append(grid[i][j])

            L.sort()

            if len(L)==1:
                return 0
                
            m=10**11

            for i in range(len(L)-1):
                m=min(m,abs(L[i]-L[i+1]))

            return m

        ans=[[0]*(len(grid[0])-k+1) for i in range(len(grid)-k+1)]
        
        if k==1:
            return ans

        for i in range(len(grid)-k+1):
            for j in range(len(grid[0])-k+1):
                ans[i][j]=asm([i,j])

        return ans        