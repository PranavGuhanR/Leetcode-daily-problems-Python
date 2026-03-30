class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1e=[s1[i] for i in range(0,len(s1),2)]
        s1o=[]
        if len(s1)!=1:
            s1o=[s1[i] for i in range(1,len(s1),2)]
        s1e.sort()
        s1o.sort()
        s2e=[s2[i] for i in range(0,len(s2),2)]
        s2o=[]
        if len(s2)!=1:
            s2o=[s2[i] for i in range(1,len(s2),2)]
        s2e.sort()
        s2o.sort()      

        if s1e==s2e:
            if s1o==s2o:
                return True
        return False          