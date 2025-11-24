class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s=0
        l=[False]*len(nums)
        for i in range(len(nums)):
            s*=2
            s+=nums[i]
            if s%5==0:
                l[i]=True
        return l        