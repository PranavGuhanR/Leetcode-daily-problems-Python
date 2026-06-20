class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        mx=0
        restrictions.sort()
        R=[0]*len(restrictions)
        if restrictions==[]:
            return n-1
        rm=n-1
        N=len(restrictions)
        rp=n
        for i in range(N-1,-1,-1):
            cp=restrictions[i][0]
            R[i]=min(rm+rp-cp,restrictions[i][1])
            rp=cp
            rm=R[i]      
        mx=0
        def mm(lv,rv,j):
            if lv==rv:
                return lv+j//2
            if lv>rv:
                lv,rv=rv,lv  
            return rv+(j-rv+lv)//2 
        lm=0
        N=len(restrictions)
        cp=restrictions[0][0]
        lp=1
        R[0]=min(cp-lp,R[0]) 
        mx=max(mm(R[0],0,cp-lp),mx) 
        lp=cp                
        for i in range(1,N):
            cp=restrictions[i][0]
            R[i]=min(R[i-1]+cp-lp,R[i])
            mx=max(mm(R[i],R[i-1],cp-lp),mx)  
            lp=cp
        if restrictions[-1][0]!=n:
            cp=n
            ev=min(R[-1]+cp-lp,n-1)
            mx=max(mm(R[-1],ev,cp-lp),mx)                                  
        return mx    