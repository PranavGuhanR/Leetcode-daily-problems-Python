class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def isMS(s,S):
            total=h[s[0]][s[1]+S]-h[s[0]][s[1]]  
            for i in range(1,S):
                if total!=h[s[0]+i][s[1]+S]-h[s[0]+i][s[1]]:
                    return 0
            for i in range(S):
                if total!=v[s[0]+S][s[1]+i]-v[s[0]][s[1]+i]:
                    return 0
            tl=0        
            for i in range(S):
                tl+=grid[s[0]+i][s[1]+i]
            if tl!=total:
                return 0                     
            bd=0        
            for i in range(S):
                bd+=grid[s[0]+S-1-i][s[1]+i]
            if bd!=total:
                return 0    
            return 1
        h=[[0]*(len(grid[0])+1) for i in range(len(grid))] 
        v=[[0]*len(grid[0]) for i in range(len(grid)+1)]    
        for i in range(len(h)):
            for j in range(1,len(grid[0])+1):
                h[i][j]=h[i][j-1]+grid[i][j-1]               
        for i in range(1,len(v)):
            for j in range(len(grid[0])):
                v[i][j]=v[i-1][j]+grid[i-1][j]   
        SS=min(len(grid),len(grid[0]))
        while SS>1:
            for i in range(len(grid)-SS+1):
                for j in range(len(grid[0])-SS+1):  
                    if isMS([i,j],SS):
                        return SS
            SS-=1            
        return 1                              