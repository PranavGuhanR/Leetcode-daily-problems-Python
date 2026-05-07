class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        pma=[nums[0]]*len(nums)
        smi=[nums[-1]]*len(nums)
        for i in range(1,len(nums)):
            pma[i]=max(pma[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            smi[i]=min(smi[i+1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            if pma[i]>smi[i+1]:
                pma[i]=pma[i+1]
        return pma        

