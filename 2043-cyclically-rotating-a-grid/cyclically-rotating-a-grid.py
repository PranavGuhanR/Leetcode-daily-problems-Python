class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def rl(L,K):
            return L[len(L)-K:]+L[:len(L)-K]

        m=len(grid)
        n=len(grid[0])
        nl=min(m//2,n//2)
        ans=[[0]*n for i in range(m)]

        for l in range(nl):
            s=2*(m+n-4*l-2)
            li=[0]*s

            e=0

            for i in range(l,m-l-1):
                li[e]=grid[i][l]
                e+=1

            for j in range(l,n-l-1):
                li[e]=grid[m-l-1][j]
                e+=1

            for i in range(m-l-1,l,-1):
                li[e]=grid[i][n-l-1]
                e+=1      

            for j in range(n-l-1,l,-1):
                li[e]=grid[l][j]
                e+=1

            rk=k%(s)

            rli=rl(li,rk)

            e=0

            for i in range(l,m-l-1):
                ans[i][l]=rli[e]
                e+=1

            for j in range(l,n-l-1):
                ans[m-l-1][j]=rli[e]
                e+=1

            for i in range(m-l-1,l,-1):
                ans[i][n-l-1]=rli[e]
                e+=1      

            for j in range(n-l-1,l,-1):
                ans[l][j]=rli[e]
                e+=1

        return ans