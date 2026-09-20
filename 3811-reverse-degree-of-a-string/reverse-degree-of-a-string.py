class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i,c in enumerate(s):
            v=ord(c)-ord('a') 
            v=26-v
            ans+=(i+1)*v
        return ans    