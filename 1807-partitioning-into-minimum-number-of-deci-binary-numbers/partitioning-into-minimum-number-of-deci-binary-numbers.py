class Solution:
    def minPartitions(self, n: str) -> int:
        max_n = 0
        for c in n:
            n = int(c)
            if n>max_n:
                max_n = n
            if max_n==9:
                return 9
        return max_n