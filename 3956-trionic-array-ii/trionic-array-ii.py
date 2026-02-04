class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        NEG = -10**18

        dp = [[NEG] * n for _ in range(4)]
        dp[0][0] = nums[0]
        ans = NEG

        for i in range(1, n):
            dp[0][i] = nums[i]

            if nums[i] > nums[i - 1]:
                dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + nums[i]
                dp[3][i] = max(dp[2][i - 1], dp[3][i - 1]) + nums[i]

            elif nums[i] < nums[i - 1]:
                dp[2][i] = max(dp[1][i - 1], dp[2][i - 1]) + nums[i]

            ans = max(ans, dp[3][i])

        return ans