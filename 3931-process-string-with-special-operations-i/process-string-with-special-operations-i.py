class Solution:
    def processStr(self, s: str) -> str:
        ans=''
        for i in range(len(s)):
            if s[i]=="%":
                ans=ans[::-1]
            elif s[i]=="*": 
                if ans!="":
                    ans=ans[:len(ans)-1]   
            elif s[i]=="#":
                ans*=2
            else:
                ans+=s[i]      
        return ans          