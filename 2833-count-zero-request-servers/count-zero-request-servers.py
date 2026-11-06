class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda p: p[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        cnt = [0] * (n + 1)
        res = [0] * len(queries)
        distinct = l = r = 0
        m = len(logs)

        for id in order:
            t = queries[id]
            while r < m and logs[r][1] <= t:
                if cnt[logs[r][0]] == 0:
                    distinct += 1
                cnt[logs[r][0]] += 1
                r += 1
            while l < r and logs[l][1] < t - x:
                cnt[logs[l][0]] -= 1
                if cnt[logs[l][0]] == 0:
                    distinct -= 1
                l += 1
            res[id] = n - distinct
        return res