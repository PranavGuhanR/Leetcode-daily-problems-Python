from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits, startPos: int, k: int) -> int:
        positions = [p for p, _ in fruits]
        prefix = [0] * (len(fruits) + 1)

        for i in range(len(fruits)):
            prefix[i + 1] = prefix[i] + fruits[i][1]

        def get_sum(left, right):
            l = bisect_left(positions, left)
            r = bisect_right(positions, right) - 1
            if l > r:
                return 0
            return prefix[r + 1] - prefix[l]

        res = 0

        for x in range(k + 1):
            left = startPos - x
            right = startPos + (k - 2 * x)
            if left > right:
                break
            res = max(res, get_sum(left, right))

        for x in range(k + 1):
            right = startPos + x
            left = startPos - (k - 2 * x)
            if left > right:
                break
            res = max(res, get_sum(left, right))

        return res