class Solution:
    def maxOperations(self, s: str) -> int:
        c=0
        ans=0
        for i in range(len(s)-1):
            if s[i]=='1':
                c+=1
            if s[i]=='1' and s[i+1]=='0':
                ans+=c
        return ans