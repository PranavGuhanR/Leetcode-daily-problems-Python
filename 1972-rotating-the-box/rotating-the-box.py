class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m=len(boxGrid)
        n=len(boxGrid[0])
        ans=[[0]*m for i in range(n)]
        for i in range(len(boxGrid)):
            s=len(boxGrid[0])-1
            e=len(boxGrid[0])-1
            while True:
                d={".":0,"#":0}                
                while e>=0 and  boxGrid[i][e]!="*":
                    d[boxGrid[i][e]]+=1  
                    e-=1
                else:
                    for j in range(d["#"]):
                        ans[s-j][m-1-i]="#"

                    for j in range(d["."]):
                        ans[s-d["#"]-j][m-1-i]="."   
                        
                    if e<0:
                        break                             
                    else:  
                        ans[e][m-1-i]="*"
                        e-=1 
                        s=e   
   
        return ans