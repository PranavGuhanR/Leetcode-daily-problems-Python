class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))

        def dpu():
            prev = [float("-inf")] * n
            curr = [float("-inf")] * n
            prev[n - 1] = fruits[0][n - 1]
            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[i][j]
                prev, curr = curr, prev
            return prev[n - 1]
        def dpl():
            prev = [float("-inf")] * n
            curr = [float("-inf")] * n
            prev[n - 1] = fruits[n - 1][0]
            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[j][i]
                prev, curr = curr, prev
            return prev[n - 1]
        ans += dpu()+dpl()
        return ans