class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        for i in range(len(nums)):
            result[i]=nums[(i+nums[i])%len(nums)]
        return result    