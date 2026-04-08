class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for i in range(len(queries)):
            for j in range(queries[i][0],queries[i][1]+1,queries[i][2]):
                nums[j]=(nums[j]*queries[i][3])%(10**9+7)  

        ans=nums[0]

        if len(nums)!=1:
            for e in nums[1::]:
                ans^=e
                
        return ans        