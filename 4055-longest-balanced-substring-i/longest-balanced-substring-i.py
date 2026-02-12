class Solution:
    def longestBalanced(self, s: str) -> int:
        m=1 
        for i in range(len(s)):
            dc=dict()
            dl=dict()
            for j in range(i,len(s)):
                if s[j] in dl:
                    if dc[dl[s[j]]]==1:
                        del dc[dl[s[j]]]
                    else:
                        dc[dl[s[j]]]-=1
                    dl[s[j]]+=1    
                else:
                    dl[s[j]]=1   
                if dl[s[j]] in dc:
                    dc[dl[s[j]]]+=1
                else:
                    dc[dl[s[j]]]=1  
                if len(dc)==1:
                    if j-i+1>m:
                        m=j-i+1  
        return m