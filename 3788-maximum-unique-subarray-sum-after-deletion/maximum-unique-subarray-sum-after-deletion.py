class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=set()
        ans=0
        ma=nums[0]
        for i in nums:
            if i>ma:
                ma=i
            if i not in s and i>0:
                ans+=i
                s.add(i)
        if s==set():
            return ma        
        return ans        