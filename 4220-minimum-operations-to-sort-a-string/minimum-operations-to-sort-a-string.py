class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n == 2 and s[0] > s[1]:
            return -1
        for ch1, ch2 in pairwise(s):
            if ch1 > ch2:
                break
        else:
            return 0
        mn, mx = min(s[1:-1]), max(s[1:-1])
        left, right = s[0], s[~0]
            
        if left <= min(right, mn) or right >= max(left, mx):
            return 1
        elif right >= mn or left <= mx:
            return 2
        else:
            return 3