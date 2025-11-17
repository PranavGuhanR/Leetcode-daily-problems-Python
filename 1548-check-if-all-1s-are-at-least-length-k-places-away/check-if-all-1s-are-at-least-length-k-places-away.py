class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        g=0
        f=0
        for i in range(len(nums)):
            if f:
                if nums[i]==0:
                    g+=1
                else:
                    if g<k:
                        return False
                    g=0 
            elif nums[i]==1:
                f=1
        return True                               