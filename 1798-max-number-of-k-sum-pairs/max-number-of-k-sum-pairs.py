class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1 
        c=0          
        for i in d:
            if k-i in d:
                c+=min(d[i],d[k-i])
        return c//2                         