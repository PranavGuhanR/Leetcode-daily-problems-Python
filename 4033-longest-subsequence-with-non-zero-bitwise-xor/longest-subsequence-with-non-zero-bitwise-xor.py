class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xr=0
        c=0
        for i in nums:
            if i!=0:
                xr^=i  
                c+=1      
        ans=len(nums)
        if xr==0:
            ans-=1
        if c:    
            return ans    
        return 0    