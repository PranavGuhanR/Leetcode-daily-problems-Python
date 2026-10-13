class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sq = [x * x for x in nums]
        return sum(sq) - 2 * self.sum_smallest(sq, len(sq) // 2) 
    def sum_smallest(self, a: list[int], k: int) -> int:  
        if k == 0:
            return 0
        pivot = random.choice(a)
        lo = [x for x in a if x < pivot]
        if k <= len(lo):
            return self.sum_smallest(lo, k)  
        take = min(k - len(lo), a.count(pivot))  
        hi = [x for x in a if x > pivot]
        return sum(lo) + take * pivot + self.sum_smallest(hi, k - len(lo) - take)  