class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            if num % 2:
                ans[i] = (num - ((num + 1) & (-num - 1)) // 2)
        return ans