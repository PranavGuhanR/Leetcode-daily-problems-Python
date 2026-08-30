class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return len(nums)

        s=0
        sv=nums[s]    
        l=0
        lv=nums[l]  
        for i in range(1,len(nums)):
            if sv>nums[i]:
                s=i
                sv=nums[s]
            elif lv<nums[i]:
                l=i
                lv=nums[l] 

        return min(max(s+1,l+1),max(len(nums)-s,len(nums)-l),min(s,l)+1+min(len(nums)-s,len(nums)-l))               