class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def s(n):
            sum=0
            while n:
                sum+=n%10
                n//=10
            return sum    
        for i in range(len(nums)):
            if s(nums[i])==i:
                return i
        return -1               