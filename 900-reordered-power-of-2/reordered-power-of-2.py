class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def p2(N):
            pt=1
            while N>=pt:
                if pt==N:
                    return 1
                pt*=2
            return 0        
        def p(s,l,cs,r):
            if l==len(s):
                if p2(int(cs)):
                    return 1
                return 0
            for i in r.keys():
                if not (l==0 and i=='0') and r[i]!=0:
                    r[i]-=1  
                    if p(s,l+1,cs+i,r):
                        return 1     
                    r[i]+=1       
        rem=dict()
        for i in str(n):
            if i in rem:
                rem[i]+=1
            else:
                rem[i]=1
        if p(str(n),0,'',rem):
            return True
        return False               