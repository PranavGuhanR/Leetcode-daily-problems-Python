class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s=[nums[-1]]*len(nums)
        p=nums[0]
        for i in range(len(nums)-2,0,-1):
            s[i]=max(s[i+1],nums[i+1])
        for i in range(1,len(nums)-1):
            if nums[i]<s[i] and p<nums[i]:
                return True
            p=min(p,nums[i])      
        return False    