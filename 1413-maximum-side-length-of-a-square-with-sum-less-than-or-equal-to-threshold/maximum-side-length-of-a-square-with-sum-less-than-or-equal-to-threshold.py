class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def isOK(s,S):
            total=h[s[0]][s[1]+S]-h[s[0]][s[1]]
            for i in range(1,S):
                total+=h[s[0]+i][s[1]+S]-h[s[0]+i][s[1]]
            if total<=threshold:
                return 1
            return 0
        h=[[0]*(len(mat[0])+1) for i in range(len(mat))] 
        for i in range(len(mat)):
            for j in range(1,len(mat[0])+1):
                h[i][j]=h[i][j-1]+mat[i][j-1]  
        r=min(len(mat),len(mat[0])) 
        l=1 
        ans=0      
        while l<=r:
            f=0 
            CS=(l+r)//2                
            for i in range(len(mat)-CS+1):
                if f==0:
                    for j in range(len(mat[0])-CS+1):
                        if isOK([i,j],CS):
                            ans=max(ans,CS)
                            l=CS+1
                            f=1
                            break
                else:
                    break   
            if f==0:                 
                r=CS-1            
        return ans               