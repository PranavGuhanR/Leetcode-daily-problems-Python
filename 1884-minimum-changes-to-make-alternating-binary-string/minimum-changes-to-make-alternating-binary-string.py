class Solution:
    def minOperations(self, s: str) -> int:
        e=len(s)//2
        o=e+len(s)%2
        e1=0
        o1=0
        for i in range(0,len(s),2):
            if s[i]=='1':
                o1+=1
        for i in range(1,len(s),2):
            if s[i]=='1':
                e1+=1        
        return min(o-o1+e1,e-e1+o1)                       