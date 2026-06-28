class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        arr.sort()    
        p=1    
        for i in range(1,len(arr)):
            arr[i]=min(arr[i],p+1)   
            p=arr[i] 
        return arr[-1]    