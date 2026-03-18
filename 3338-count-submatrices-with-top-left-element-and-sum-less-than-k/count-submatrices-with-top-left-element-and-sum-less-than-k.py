class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        for i in range(len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=grid[i][j-1]
        pj=len(grid[0])-1    
        c=0   
        for j in range(len(grid[0])-1,-1,-1):
            if grid[0][j]<=k:
                c+=j+1
                pj=j
                break
        i=1       
        while i<len(grid):
            j=pj
            while j>-1:
                grid[i][j]=grid[i-1][j]+grid[i][j]
                if grid[i][j]<=k:
                    c+=1
                else:
                    pj-=1
                j-=1    
            i+=1        
        return c