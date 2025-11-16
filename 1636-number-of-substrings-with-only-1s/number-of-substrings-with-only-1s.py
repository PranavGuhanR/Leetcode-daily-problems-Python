class Solution:
    def numSub(self, s: str) -> int:
        m=10**9+7
        def cts(n):
            return ((n%m)*((n+1)%m)//2)%m
        c=0 
        if s=='1':
            return 1
        if s=='0':
            return 0   
        ones=0 
        if s[0]=='1':
            ones+=1    
        for i in range(1,len(s)):
            if s[i-1]=='1':
                if s[i]=='0':
                    c=(c+cts(ones))%m
                    ones=0
            if s[i]=='1':
                ones+=1   
        if s[-1]=='1':
            c=(c+cts(ones))%m            
        return c