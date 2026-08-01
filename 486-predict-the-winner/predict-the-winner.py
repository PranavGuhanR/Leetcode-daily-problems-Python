class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def wsa(l,r):
            if l==r:
                return [nums[l],0]
            r1=wsa(l,r-1)            
            r2=wsa(l+1,r)
            if r1[1]+nums[r]>r2[1]+nums[l]:
                return [r1[1]+nums[r],r1[0]]
            return [r2[1]+nums[l],r2[0]] 

        ansl=wsa(0,len(nums)-1)  

        if ansl[0]>=ansl[1]:
            return True  
        return False