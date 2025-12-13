class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ansd={'electronics':[],'grocery':[],'pharmacy':[],'restaurant':[]}
        for i in range(len(code)):
            f=0
            if code[i]=='':
                continue
            for j in code[i]:
                if (not j.isalnum()) and j!='_':
                    f=1
                    break
            if f:
                continue 
            if not isActive[i]:
                continue
            if businessLine[i] not in ansd.keys():
                continue
            else:
                ansd[businessLine[i]].append(code[i])               
        ans=[]
        for i in ansd.keys():
            ansd[i].sort()
            ans+=ansd[i]
        return ans