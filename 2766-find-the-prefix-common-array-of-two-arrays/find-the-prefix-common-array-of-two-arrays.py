class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans=[0]*len(A)
        if A[0]==B[0]:
            ans[0]=1
        a=set([A[0]])  
        b=set([B[0]])  
        for i in range(1,len(A)):
            ans[i]=ans[i-1]
            if A[i]==B[i]:
                ans[i]+=1
            else:
                if A[i] in b:
                    ans[i]+=1 
                else:
                    a.add(A[i])         
                if B[i] in a:
                    ans[i]+=1 
                else:
                    b.add(B[i])         
        return ans                             