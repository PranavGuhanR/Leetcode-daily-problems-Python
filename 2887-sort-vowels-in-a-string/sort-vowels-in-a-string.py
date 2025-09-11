class Solution:
    def sortVowels(self, s: str) -> str:
        li=set()
        lv=[]
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                li.add(i)
                lv.append(s[i])
        lv.sort()
        ans=[]
        idx=0
        for i in range(len(s)):
            if i in li:
                ans.append(lv[idx])
                idx+=1
            else:
                ans.append(s[i])
        return "".join(ans)            


