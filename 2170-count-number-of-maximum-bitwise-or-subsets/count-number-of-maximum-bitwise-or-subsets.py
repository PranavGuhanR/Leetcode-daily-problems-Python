class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        br=ans=0
        for i in nums:
            br=br | i
        for i in range(2**len(nums)):
            b=0
            for j in range(len(nums)):
                if (i>>j)%2:
                    b=b | nums[j]
            if b==br:
                ans+=1
        return ans        