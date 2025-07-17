class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp=[]
        m=0
        for i in range(k):
            dp+=[[0 for j in range(k)]]
        for i in range(len(nums)):
            cn=nums[i]%k
            for j in range(k):
                dp[j][cn]=dp[j][(k+j-cn)%k]+1
                m=max(m,dp[j][cn])   
        return m        