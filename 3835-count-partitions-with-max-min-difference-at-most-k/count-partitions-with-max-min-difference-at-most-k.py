from collections import deque
class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxd = deque()
        mind = deque()
        start_index = 0
        p = [0] * (n + 1)
        dp = 1
        p[0] = 1

        for curr_index in range(0, n):
            x = nums[curr_index]
            while maxd and maxd[-1] < x:
                maxd.pop()
            maxd.append(x)
            while mind and mind[-1] > x:
                mind.pop()
            mind.append(x)
            while maxd[0] - mind[0] > k:
                if nums[start_index] == maxd[0]:
                    maxd.popleft()
                if nums[start_index] == mind[0]:
                    mind.popleft()
                start_index += 1
            dp = (p[curr_index] - (p[start_index-1] if start_index > 0 else 0)) % (10**9+7)
            p[curr_index+1] = (p[curr_index] + dp) % (10**9+7)
        return dp