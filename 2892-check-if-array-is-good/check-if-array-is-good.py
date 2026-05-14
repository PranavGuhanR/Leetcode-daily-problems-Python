class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        l1=[i+1 for i in range(n-1)]
        l1.append(n-1)
        v1=Counter(nums)
        v2=Counter(l1)

        if v1==v2:
            return True

        return False          