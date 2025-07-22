class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        ans = nums[0]
        cur = 0
        j = 0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[j])
                cur -= nums[j]
                j += 1
            s.add(nums[i])
            cur += nums[i]
            ans = max(ans, cur)
        return ans