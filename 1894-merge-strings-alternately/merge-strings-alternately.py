class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        i=j=0
        s=''
        while i<n1 and j<n2:
            s+=word1[i]+word2[j]
            i+=1
            j+=1
        if n1==n2:
            return s
        if n1>n2:
            return s+word1[i::]
        return s+word2[j::]