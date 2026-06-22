class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in text:
            if i in d:
                d[i]+=1
        m=10**4
        for i in d.keys():
            if i not in "ol":
                m=min(m,d[i])
            else:
                m=min(m,d[i]//2)  
        return m 