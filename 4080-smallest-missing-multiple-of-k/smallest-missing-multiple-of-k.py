class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set([i*k for i in range(1,len(nums)+2)])
        for e in nums:
            if e in s:
                s.remove(e)
        return min(s)                