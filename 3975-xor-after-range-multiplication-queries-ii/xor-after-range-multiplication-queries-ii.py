from collections import defaultdict
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        updates = defaultdict(lambda: defaultdict(list))

        for l, r, k, v in queries:
            rem = l % k
            start = (l - rem) // k
            end = (r - rem) // k
            updates[k][rem].append((start, end, v))

        mult = [1] * n

        for k in updates:
            for rem in updates[k]:
                size = (n - rem + k - 1) // k
                diff = [1] * (size + 1)

                for s, e, v in updates[k][rem]:
                    diff[s] = diff[s] * v % MOD
                    if e + 1 < len(diff):
                        diff[e + 1] = diff[e + 1] * pow(v, MOD - 2, MOD) % MOD

                cur = 1
                for i in range(size):
                    cur = cur * diff[i] % MOD
                    idx = rem + i * k
                    if idx < n:
                        mult[idx] = mult[idx] * cur % MOD

        for i in range(n):
            nums[i] = nums[i] * mult[i] % MOD

        ans = 0
        for x in nums:
            ans ^= x

        return ans