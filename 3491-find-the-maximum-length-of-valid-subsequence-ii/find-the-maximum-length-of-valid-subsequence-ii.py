class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp=[]
        m=0
        for i in range(k):
            dp+=[[0 for j in range(k)]]   #dp[j][cn]- for any particular i, 
                                          #length of the longest subsequence 
                                          #possible out of nums[0:i+1] ending 
                                          #with a number cn as nums[i]%k 
                                          #and sum of adjacent numbers % k as j  
        for i in range(len(nums)):
            cn=nums[i]%k
            for j in range(k):
                dp[j][cn]=dp[j][(k+j-cn)%k]+1
                m=max(m,dp[j][cn])   
        return m        
