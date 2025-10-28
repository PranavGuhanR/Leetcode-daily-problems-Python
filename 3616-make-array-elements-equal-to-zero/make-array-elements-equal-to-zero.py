class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        if len(nums)==1:
            if nums==[0]:
                return 2
            return 0  
        if len(nums)==2:
            if nums in [[0,1],[1,0]] :
                return 1
            if nums==[0,0]:
                return 4
            return 0            
        nums1=[nums[0]]   
        c=0
        for i in range(1,len(nums)):
            nums1.append(nums1[-1]+nums[i])   
        if nums[-1]==0:
            if nums1[-2]==0:
                c+=2   
            elif nums1[-2]==1:
                c+=1    
        for i in range(len(nums)-2,0,-1):
            cv=nums[i]
            nums[i]+=nums[i+1]
            if cv==0:
                if nums1[i-1]==nums[i+1]:
                    c+=2
                elif nums1[i-1]==nums[i+1]+1:
                    c+=1
                elif nums1[i-1]+1==nums[i+1]:       
                    c+=1 
        if nums[0]==0:             
            nums[0]+=nums[1]   
            if nums[0]==0:
                c+=2
            elif nums[0]==1:
                c+=1    
        return c             