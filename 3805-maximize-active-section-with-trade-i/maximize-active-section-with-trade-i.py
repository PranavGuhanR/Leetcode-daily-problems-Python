class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        count=int(s[0])
        pz=0
        cz=1-count
        AddOn=0
        for i in range(1,len(s)):
            if s[i]=="1":
                if s[i-1]=="0":
                    if pz and cz:
                        AddOn=max(AddOn,pz+cz)
                    pz=cz
                    cz=0
                count+=1
            else:
                cz+=1
        if pz and cz:
            AddOn=max(AddOn,pz+cz)    
        return count+AddOn                