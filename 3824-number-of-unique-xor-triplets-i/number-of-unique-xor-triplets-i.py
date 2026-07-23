class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==2:
            return 2
        elif len(nums)==3:
            return 4
        p=4
        l=len(nums)
        while l>=p:
            p*=2
        return p 