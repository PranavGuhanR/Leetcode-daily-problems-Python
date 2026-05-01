class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        if len(nums)==1:
            return 0

        pt=0

        for i in range(len(nums)):
            pt+=i*nums[i]

        m=pt
        s=sum(nums)

        for i in range(len(nums)-1):
            ct=pt+s-(len(nums))*nums[-i-1]
            m=max(ct,m)
            pt=ct

        return m