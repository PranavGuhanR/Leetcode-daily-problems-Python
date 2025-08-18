class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        nums = [float(c) for c in cards]
        return self.solve(nums)

    def solve(self, nums):
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24.0) < 1e-6
        for i in range(n):
            for j in range(i+1, n):
                next_nums = [nums[k] for k in range(n) if k != i and k != j]
                a, b = nums[i], nums[j]

                candidates = [a+b, a-b, b-a, a*b]
                if abs(b) > 10**(-6): candidates.append(a/b)
                if abs(a) > 10**(-6): candidates.append(b/a)
                for val in candidates:
                    next_nums.append(val)
                    if self.solve(next_nums):
                        return True
                    next_nums.pop()
        return False