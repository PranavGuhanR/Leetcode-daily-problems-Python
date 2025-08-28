class Solution:
    def sortMatrix(self, g: List[List[int]]) -> List[List[int]]:
        if len(g)==1:
            return g
        nj=len(g)-2
        while nj>0:
            i=0
            j=nj
            l=[]
            while j<=len(g)-1:
                l+=[g[i][j]]
                j+=1
                i+=1
            l.sort()
            i=0
            j=nj
            while j<=len(g)-1:
                g[i][j]=l[i]
                j+=1
                i+=1
            nj-=1    
        ni=0
        while ni<=len(g)-1:
            j=0
            i=ni
            l=[]
            while i<=len(g)-1:
                l+=[g[i][j]]
                i+=1
                j+=1
            l.sort(reverse=True)
            j=0
            i=ni
            while i<=len(g)-1:
                g[i][j]=l[j]
                j+=1
                i+=1
            ni+=1   
        return g         