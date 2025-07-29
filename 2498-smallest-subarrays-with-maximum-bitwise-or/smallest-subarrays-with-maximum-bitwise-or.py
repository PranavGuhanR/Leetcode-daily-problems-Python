class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            bo = nums[i]
            ans[i] = 1
            j = i - 1
            while j >= 0 and (nums[j] | bo != nums[j]):
                ans[j] = i - j + 1
                nums[j] |= bo
                j -= 1
        return ans