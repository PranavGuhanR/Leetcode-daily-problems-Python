class Solution:
    def bitwiseComplement(self, n: int) -> int:
        p2=2
        while p2-1<n:
            p2*=2
        return p2-1-n