class Solution:
    def minElement(self, nums: List[int]) -> int:
        m=10**4
        for i in range(len(nums)):
            v=0
            while nums[i]:
                v+=nums[i]%10
                nums[i]//=10
            nums[i]=v
            m=min(m,v)
        return m       