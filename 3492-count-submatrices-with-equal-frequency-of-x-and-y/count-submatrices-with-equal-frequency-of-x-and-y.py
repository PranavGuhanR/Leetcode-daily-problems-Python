class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        hpm=[[[0,0] for j in range(len(grid[0]))] for i in range(len(grid))]
        
        for i in range(len(grid)):
            if grid[i][0]=='X':
                hpm[i][0][0]=1
            elif grid[i][0]=='Y':
                hpm[i][0][1]=1   

        for i in range(len(grid)):
            for j in range(1,len(grid[0])):
                hpm[i][j][0]=hpm[i][j-1][0]
                hpm[i][j][1]=hpm[i][j-1][1]
                if grid[i][j]=='X':
                    hpm[i][j][0]+=1
                elif grid[i][j]=='Y':
                    hpm[i][j][1]+=1  

        c=0

        for j in range(len(grid[0])):
            if hpm[0][j][0]==hpm[0][j][1] and hpm[0][j][0]>0:
                c+=1                                   
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                hpm[i][j][0]+=hpm[i-1][j][0]
                hpm[i][j][1]+=hpm[i-1][j][1] 
                if hpm[i][j][0]==hpm[i][j][1] and hpm[i][j][0]>0:
                    c+=1                      

        return c            