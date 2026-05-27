class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        uc=set()
        lc=set()
        d=dict()
        for i in word:
            if i>='a':
                if chr(ord(i)-ord('a')+ord('A')) in uc:
                    d[i]=0
                lc.add(i)    
            else:
                if chr(ord(i)-ord('A')+ord('a')) in lc:
                    if chr(ord(i)-ord('A')+ord('a')) not in d:
                        d[chr(ord(i)-ord('A')+ord('a'))]=1
                uc.add(i)        
        return sum(d.values())      