class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])

        pos = [0] * n

        values = [0] * n

        for i in range(n):
            values[i] = nums[order[i]]
            pos[order[i]] = i

        LOG = max(1, n.bit_length())

        jump = [[0] * n for _ in range(LOG)]

        r = 0

        for i in range(n):
            if r < i:
                r = i

            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1

            jump[0][i] = r

        for p in range(1, LOG):
            for i in range(n):
                jump[p][i] = jump[p - 1][jump[p - 1][i]]

        answer = []

        for u, v in queries:
            left = pos[u]
            right = pos[v]

            if left > right:
                left, right = right, left

            if left == right:
                answer.append(0)
                continue

            current = left
            distance = 0

            for p in range(LOG - 1, -1, -1):
                if jump[p][current] < right:
                    current = jump[p][current]
                    distance += 1 << p

            if jump[0][current] >= right:
                answer.append(distance + 1)
            else:
                answer.append(-1)

        return answer