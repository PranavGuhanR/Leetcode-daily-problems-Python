class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=[0]*len(nums)
        for i in range(1,len(nums)):
            ls[i]=ls[i-1]+nums[i-1]
        rs=0
        ans=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            ans[i]=abs(ls[i]-rs)
            rs+=nums[i]
        return ans      