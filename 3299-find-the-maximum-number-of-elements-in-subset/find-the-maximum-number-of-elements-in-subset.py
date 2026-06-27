class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        m=1        
        for i in d:
            j=0
            c=1
            if i==1:
                m=max(m,d[1]-(d[1]+1)%2)
                continue
            while i**(2**(j+1))<=10**9 and i**(2**(j+1)) in d:
                if d[i**(2**j)]>=2 and d[i**(2**(j+1))]>=1:
                    c+=2
                    m=max(m,c)
                    j+=1
                else:
                    break  
        return m