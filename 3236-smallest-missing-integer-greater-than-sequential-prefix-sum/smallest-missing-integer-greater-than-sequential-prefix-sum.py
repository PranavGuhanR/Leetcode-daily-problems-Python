class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s=set(nums)
        sum=nums[0]
        i=0
        while i<len(nums)-1 and nums[i]+1==nums[i+1]:
            sum+=nums[i+1]
            i+=1

        while sum in s:
            sum+=1

        return sum               