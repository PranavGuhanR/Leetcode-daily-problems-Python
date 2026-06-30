class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        p=[-1,-1,-1]
        ans=0
        p[ord(s[0])-ord('a')]=0
        p[ord(s[1])-ord('a')]=1
        for i in range(2,len(s)):
            if s[i]=='a':
                if p[1]<p[2]:
                    li=p[1]
                else:
                    li=p[2] 
            elif s[i]=='b':                   
                if p[0]<p[2]:
                    li=p[0]
                else:
                    li=p[2]            
            else:
                if p[0]<p[1]:
                    li=p[0]
                else:
                    li=p[1] 
            p[ord(s[i])-ord('a')]=i          
            if li==-1:
                continue
            ans+=li+1                
        return ans                                        