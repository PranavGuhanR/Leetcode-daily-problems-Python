class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        l=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                l+=[nums[i-1]]
            else:
                l+=[l[-1]]
        c=0
        s='f'
        r=nums[-1]
        for i in range(len(nums)-2,0,-1):
            if nums[i]!=nums[i+1]:
                r=nums[i+1]
            if s!='v' and l[i]>nums[i] and r>nums[i]:
                c+=1
                s='v'
            elif s!='h'and l[i]<nums[i] and r<nums[i]:
                c+=1    
                s='h'
        return c