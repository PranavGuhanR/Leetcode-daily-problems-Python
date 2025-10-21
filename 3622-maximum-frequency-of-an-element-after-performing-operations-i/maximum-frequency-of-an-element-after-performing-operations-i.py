class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = max(nums)                   # max value in nums
        count = [0] * (n + 1)           # counting sort, O(n)
        for num in nums:
            count[num] += 1
        presum = [0]                    # prefix sum
        for i in range(n + 1):
            presum.append(presum[-1] + count[i])
        ans = 0
        for i in range(n + 1):
            left = presum[i] - presum[max(0, i-k)]              # [i-k..i-1]
            right = presum[min(n+1, i+k+1)] - presum[i+1]       # [i+1..i+k]
            cur = count[i] + min(numOperations, left + right)   # at most numOperations
            ans = max(ans, cur)                                 # update ans
        return ans