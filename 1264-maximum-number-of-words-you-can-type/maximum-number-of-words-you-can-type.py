class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        c=0
        s=set([i for i in brokenLetters])
        for i in l:
            for j in i:
                if j in s:
                    c+=1
                    break
        return len(l)-c            