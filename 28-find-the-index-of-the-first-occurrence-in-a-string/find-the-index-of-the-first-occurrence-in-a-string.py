class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        count = 0
        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] == needle[j]:
                    count += 1
                else:
                    count = 0
                    break
                if n == count:
                    return i

        return -1
        