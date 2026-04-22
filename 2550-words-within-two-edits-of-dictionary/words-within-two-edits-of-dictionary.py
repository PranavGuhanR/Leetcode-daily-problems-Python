class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans=[]
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                um=0
                f=1
                for k in range(len(queries[0])):
                    if queries[i][k]!=dictionary[j][k]:
                        um+=1
                        if um==3:
                            f=0
                            break
                if f:
                    ans.append(queries[i])
                    break

        return ans         