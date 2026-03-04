class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        s=dict()
        ans=0
        for i in range(len(mat)):
            c=0
            ne=(0,0)
            f=1
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    c+=1
                    if c==2:
                        f=0
                        break
                    else:
                        ne=(i,j)  
            if f:              
                s[ne]=1            
        for j in range(len(mat[0])):
            c=0
            ne=(-1,-1)
            f=1
            for i in range(len(mat)):
                if mat[i][j]==1:
                    c+=1
                    if c==2:
                        f=0
                        break
                    else:
                        ne=(i,j)  
            if f and (ne in s):
                ans+=1   

        return ans               