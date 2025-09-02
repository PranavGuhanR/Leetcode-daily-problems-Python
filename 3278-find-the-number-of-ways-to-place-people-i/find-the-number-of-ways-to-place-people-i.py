class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def isp(i1,i2):
            l=min(points[i1][1],points[i2][1])
            r=max(points[i1][1],points[i2][1])
            t=max(points[i1][0],points[i2][0])
            b=min(points[i1][0],points[i2][0])
            for i in range(len(points)):
                if i not in [i1,i2]:
                    if points[i][0]>=b and points[i][0]<=t and points[i][1]>=l and points[i][1]<=r and points[i][1]>=l:
                        return 0          
            return 1
        s=0
        for i1 in range(len(points)-1):
            for i2 in range(i1+1,len(points)):
                l=min(points[i1][1],points[i2][1])
                r=max(points[i1][1],points[i2][1])
                t=max(points[i1][0],points[i2][0])
                b=min(points[i1][0],points[i2][0])
                if l!=r and t!=b and (points[i1]==[t,r] or points[i2]==[t,r]):
                    continue
                if isp(i1,i2):
                    s+=1
        return s                             