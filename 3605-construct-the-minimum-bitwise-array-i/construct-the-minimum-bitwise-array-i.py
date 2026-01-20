class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        d=dict()
        for i in range(1,1001):
            k=i|(i+1)
            if k not in d:
                d[k]=i       
        ans=[-1]*len(nums) 
        for i in range(len(nums)):
            if nums[i] in d:
                ans[i]=d[nums[i]]
        return ans       