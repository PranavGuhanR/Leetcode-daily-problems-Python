class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        s=''
        for i in range(len(l)-1,0,-1):
            s+=l[i]+' '
        s+=l[0]
        return s    