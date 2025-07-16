class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c1=c2=c3=0
        if nums[0]%2:
            c1+=1       #c1- Max_length out of all the subsequences with only odd numbers for the array nums[0:i+1]
        else:           
            c2+=1       #c2- Max_length out of all the subsequences with only even numbers for the array nums[0:i+1]
        c3=1            #c3- Max_length out of all the subsequences with altering even and odd numbers 
        pn=nums[0]%2    #pn- nums[i-1]%2        
        for i in range(1,len(nums)):
            if nums[i]%2:
                c1+=1
            else:
                c2+=1
            if nums[i]%2!=pn:
                c3+=1
                pn=nums[i]%2   
        return max(c1,c2,c3)         