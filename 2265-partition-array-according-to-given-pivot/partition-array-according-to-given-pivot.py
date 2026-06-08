class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]   
        e=[] 
        g=[] 
        for i in nums:
            if i<pivot:
                l.append(i) 
            elif i==pivot:
                e.append(i)  
            else:
                g.append(i) 
        return l+e+g              