class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pn=nums[0]
        c=mc=1
        m=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>m:
                m=nums[i]
                mc=1
                c=1
                pn=m
            elif nums[i]==m and pn==m:
                c+=1    
                mc=max(c,mc)
            else:
                c=1
                pn=nums[i]
        return mc            