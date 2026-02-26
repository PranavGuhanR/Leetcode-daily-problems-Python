class Solution:
    def numSteps(self, s: str) -> int:
        m=1
        n=0
        for i in range(-1,-len(s)-1,-1):
            if s[i]=='1':
                n+=m
            m*=2
        ans=0
        while n!=1:
            if n%2:
                n+=1
            else:
                n//=2   
            ans+=1
        return ans                 