class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cm=0
        pe=0
        m=0
        p1=0
        c1=0
        for i in nums:
            if i:
                c1+=1
            else:
                if cm==1:
                    m=max(m,p1+c1) 
                else:
                    m=max(m,c1)    
                p1=c1
                c1=0
                cm=1
        if cm==1:
            m=max(m,p1+c1)               
        else:
            m=max(m,c1)
        if m==len(nums):
            return m-1    
        return m    