class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[folder[0]]
        cur=1
        while cur<len(folder):
            n = len(res[-1])
            if res[-1]+'/'!=folder[cur][:n+1]: #If the cur folder is not
                                               #in latest elment in res,
                                               #appends the folder to re 
                                               #Else, check for the next 
                                               #folder
                res.append(folder[cur])
            cur+=1
        return res