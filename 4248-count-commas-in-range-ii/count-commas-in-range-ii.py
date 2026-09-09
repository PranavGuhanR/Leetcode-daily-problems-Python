class Solution:
    def countCommas(self, n: int) -> int:
        k = (len(str(n)) - 1) // 3 
        return k * (n + 1) - (1000**(k + 1) - 1000) // 999