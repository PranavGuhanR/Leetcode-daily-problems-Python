class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set()
        ans=0
        for i in range(len(word)):
            if word[i]>='a':
                if chr(ord(word[i])-ord('a')+ord('A')) in s:
                    if word[i] not in s:
                        ans+=1
            else:
                if chr(ord(word[i])-ord('A')+ord('a')) in s:
                    if word[i] not in s:
                        ans+=1               
            s.add(word[i])
        return ans