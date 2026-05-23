class Solution:
    def check(self, nums: List[int]) -> bool:
        mm=nums[0]
        m=nums[0]
        ci=-1
        for i in range(1,len(nums)):
            if m > nums[i]:
                ci=i
                if nums[i]>mm:
                    return False
                break
            m=nums[i] 
        if ci==-1:
            return True       
        for i in range(ci+1, len(nums)):
            if nums[i]<nums[i-1] or nums[i]>mm:
                return False
        return True         