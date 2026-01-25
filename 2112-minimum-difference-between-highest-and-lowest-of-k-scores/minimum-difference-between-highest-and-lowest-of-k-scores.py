class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        d=nums[k-1]-nums[0]
        for i in range(1,len(nums)-k+1):
            d=min(d,nums[i+k-1]-nums[i])
        return d    