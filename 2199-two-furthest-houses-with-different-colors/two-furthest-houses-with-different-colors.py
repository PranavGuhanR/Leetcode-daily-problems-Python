class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d=dict()
        m=0
        for i in range(len(colors)):
            if colors[i] in d:
                m=max(m,i-d[colors[i]])
            else:
                if colors[0]!=colors[i]:
                    d[colors[i]]=0
                    m=max(m,i)
                    if colors[0] not in d:
                        d[colors[0]]=i
        return m            