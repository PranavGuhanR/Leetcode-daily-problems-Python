class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s=101
        for i in range(1,len(nums)-1):
            for j in range(i+1,len(nums)):
                cs=nums[i]+nums[j]
                if cs<s:
                    s=cs
        return s+nums[0]                 