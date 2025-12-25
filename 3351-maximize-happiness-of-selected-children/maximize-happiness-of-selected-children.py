class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        s=0
        for i in range(k):
            ce=happiness.pop()
            if ce-i<=0:
                return s
            else:
                s+=ce-i
        return s                     