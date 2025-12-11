class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        v=[[10**6,-1] for i in range(n)]
        h=[[10**6,-1] for i in range(n)]
        for i in range(len(buildings)):
            if buildings[i][0]-1<h[buildings[i][1]-1][0]:
                h[buildings[i][1]-1][0]=buildings[i][0]-1
            if buildings[i][0]-1>h[buildings[i][1]-1][1]:
                h[buildings[i][1]-1][1]=buildings[i][0]-1           
            if buildings[i][1]-1<v[buildings[i][0]-1][0]:
                v[buildings[i][0]-1][0]=buildings[i][1]-1
            if buildings[i][1]-1>v[buildings[i][0]-1][1]:
                v[buildings[i][0]-1][1]=buildings[i][1]-1     
        c=0
        for i in range(len(buildings)):
            if buildings[i][0]-1>h[buildings[i][1]-1][0]:
                if buildings[i][0]-1<h[buildings[i][1]-1][1]:           
                    if buildings[i][1]-1>v[buildings[i][0]-1][0]:
                        if buildings[i][1]-1<v[buildings[i][0]-1][1]:    
                            c+=1
        return c                          