class Window:

    def __init__(self, values):
        self.h, self.odd = len(values) // 2, len(values) & 1
        self.sorted = SortedList(values)
        self.low, self.total = sum(self.sorted[:self.h]), sum(values)

    @property
    def cost(self): 
        return self.total - 2 * self.low - self.odd * self.sorted[self.h]

    def slide(self, out, new):
        s, h = self.sorted, self.h
        if new < s[h - 1]: 
            self.low += new - s[h - 1]
        s.add(new)
        if out <= s[h - 1]: 
            self.low += s[h] - out
        s.remove(out)
        self.total += new - out
        return self.cost


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        win = Window(nums[:x])
        cost = [win.cost] + [win.slide(out, new) for out, new in zip(nums, nums[x:])]
        best = [0] * (len(nums) + 1)  
        for _ in range(k):
            best = list(accumulate([inf] * x + [b + c for b, c in zip(best, cost)], min))
        return best[-1]