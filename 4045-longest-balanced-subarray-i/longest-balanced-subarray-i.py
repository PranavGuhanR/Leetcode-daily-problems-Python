class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        m=0
        for i in range(len(nums)):
            se=set()
            so=set()
            for j in range(i,len(nums)):
                if nums[j]%2:
                    if nums[j] not in so:
                        so.add(nums[j])
                else:
                    if nums[j] not in se:
                        se.add(nums[j]) 
                if len(se)==len(so):
                    m=max(m,j-i+1)
        return m