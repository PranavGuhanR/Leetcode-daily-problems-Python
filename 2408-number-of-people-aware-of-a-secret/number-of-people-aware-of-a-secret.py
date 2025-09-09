class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp=[0]*forget
        dp[0]=1
        cs=0
        for i in range(n-1):
            cs-=dp[-1]
            for j in range(len(dp)-1,0,-1):
                dp[j]=dp[j-1]
            cs+=dp[delay]    
            dp[0]=cs
        s=0    
        for i in dp:
            s=(s+i)%(10**9+7)    
        return s        