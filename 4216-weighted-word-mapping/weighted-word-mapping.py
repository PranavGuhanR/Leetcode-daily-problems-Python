class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def wgh(W):
            s=0
            for i in W:
                s+=weights[ord(i)-ord('a')]
            return s    
        ans=''     
        for w in words:
            ans+=chr(ord('a')+25-(wgh(w)%26))
        return ans              