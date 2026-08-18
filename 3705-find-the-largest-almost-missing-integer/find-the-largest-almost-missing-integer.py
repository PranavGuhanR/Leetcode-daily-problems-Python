class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]      
        if len(nums)==k:
            return max(nums)  
        st=set()  
        if k==1:
            mt=set()   
            for e in nums:
                if e not in mt:
                    if e in st:
                        st.remove(e) 
                        mt.add(e) 
                    else: 
                        st.add(e)    
                print(st,mt)        
        else:  
            if nums[0]==nums[-1]:
                return -1   
            st.add(nums[0])
            st.add(nums[-1])
            for e in nums[1:len(nums)-1]:
                if e in st:
                    st.remove(e)
        if st:        
            return max(st) 
        return -1  