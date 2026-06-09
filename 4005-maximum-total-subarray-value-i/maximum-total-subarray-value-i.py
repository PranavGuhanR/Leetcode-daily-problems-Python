class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ma=nums[0]  
        mi=nums[0] 
        if len(nums)==1:
            return 0
        for i in nums[1::]:
            ma=max(ma,i)
            mi=min(mi,i)
        return (ma-mi)*k    
