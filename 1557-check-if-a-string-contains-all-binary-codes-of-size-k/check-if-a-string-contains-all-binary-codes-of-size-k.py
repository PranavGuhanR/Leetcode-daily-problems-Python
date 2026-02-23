class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        S=set([i for i in range(2**k)])
        b=1  
        n=0  
        for i in range(k-1,-1,-1):
            n+=int(s[i])*b 
            b*=2
        S.remove(n)
        for i in range(k,len(s)):
            n=n*2
            ns=n&(1<<k)
            n+=int(s[i]) 
            n-=ns
            if S:
                if n in S:
                    S.remove(n)
            else:
                return True    
        if S:
            return False
        return True        