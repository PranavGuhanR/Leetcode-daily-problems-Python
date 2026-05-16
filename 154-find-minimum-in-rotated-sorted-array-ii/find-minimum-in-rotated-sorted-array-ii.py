class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        m=nums[0]
        for i in nums[1:]:
            m=min(m,i)

        return m    