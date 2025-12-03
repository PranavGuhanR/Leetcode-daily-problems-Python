import math
from collections import Counter, defaultdict


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        n = len(points)
        slopes = defaultdict(lambda: defaultdict(int))
        mids = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                s = (dy, dx)
                c = dx * y1 - dy * x1
                slopes[s][c] += 1
                mid = (x1 + x2, y1 + y2)
                mids[mid][s] += 1

        tot = 0
        for line_counts in slopes.values():
            total = sum(line_counts.values())
            tot += (total **2 - sum(v **2 for v in line_counts.values())) // 2

        para = 0
        for sCnt in mids.values():
            v = sum(sCnt.values())
            if v > 1:
                para += v * (v - 1) // 2 - sum(c * (c - 1) // 2 for c in sCnt.values())

        return tot - para