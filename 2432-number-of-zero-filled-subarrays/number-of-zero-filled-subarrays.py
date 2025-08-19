class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l=ispz=ans=0
        if nums[0]==0:
            ispz=1
            l=1
        for i in range(1,len(nums)):
            if nums[i]!=0:
                if ispz:
                    ans+=l*(l+1)//2
                    l=0 
                ispz=0  
            else:
                ispz=1
                l+=1 
        ans+=l*(l+1)//2                
        return ans