class Solution:
    def countPartitions(self, a: List[int]) -> int:
        if abs(a[0]-sum(a[1::])+1)%2:
            return len(a)-1
        return 0    