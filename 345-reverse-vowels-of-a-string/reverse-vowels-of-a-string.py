class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                l+=[s[i]]
        ns=''
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                ns+=l.pop()  
            else:
                ns+=s[i]   
        return ns                       