from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words)==1:
            return words
        p=Counter(words[0])
        ansd=[p]
        ans=[words[0]]
        for i in range(1,len(words)):
            c=Counter(words[i])
            if p!=c:
                p=c
                ansd.append(c)
                ans.append(words[i])
            else:
                if ans:
                    p=ansd[-1]
                else: 
                    p=1    
        return ans        